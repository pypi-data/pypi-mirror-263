import base64
import enum
import pathlib
import sys
import time
import warnings
from typing import Any, Dict, Iterator, List, Optional, Set, Union

from determined.common import api
from determined.common.api import bindings
from determined.common.experimental import checkpoint, trial, workspace

# TODO (MLG-1087): move OrderBy to experimental.client namespace
from determined.common.experimental._util import OrderBy  # noqa: I2041


# Wrap the autogenerated bindings in something a little more ergonomic.
class ExperimentState(enum.Enum):
    ACTIVE = bindings.experimentv1State.ACTIVE.value
    PAUSED = bindings.experimentv1State.PAUSED.value
    STOPPING_COMPLETED = bindings.experimentv1State.STOPPING_COMPLETED.value
    STOPPING_CANCELED = bindings.experimentv1State.STOPPING_CANCELED.value
    STOPPING_ERROR = bindings.experimentv1State.STOPPING_ERROR.value
    COMPLETED = bindings.experimentv1State.COMPLETED.value
    CANCELED = bindings.experimentv1State.CANCELED.value
    ERROR = bindings.experimentv1State.ERROR.value
    DELETED = bindings.experimentv1State.DELETED.value
    DELETING = bindings.experimentv1State.DELETING.value
    DELETE_FAILED = bindings.experimentv1State.DELETE_FAILED.value
    STOPPING_KILLED = bindings.experimentv1State.STOPPING_KILLED.value
    QUEUED = bindings.experimentv1State.QUEUED.value
    PULLING = bindings.experimentv1State.PULLING.value
    STARTING = bindings.experimentv1State.STARTING.value
    RUNNING = bindings.experimentv1State.RUNNING.value

    def _to_bindings(self) -> bindings.experimentv1State:
        return bindings.experimentv1State(self.value)


class ExperimentSortBy(enum.Enum):
    ID = bindings.v1GetExperimentsRequestSortBy.ID
    DESCRIPTION = bindings.v1GetExperimentsRequestSortBy.DESCRIPTION
    START_TIME = bindings.v1GetExperimentsRequestSortBy.START_TIME
    END_TIME = bindings.v1GetExperimentsRequestSortBy.END_TIME
    STATE = bindings.v1GetExperimentsRequestSortBy.STATE
    NUM_TRIALS = bindings.v1GetExperimentsRequestSortBy.NUM_TRIALS
    PROGRESS = bindings.v1GetExperimentsRequestSortBy.PROGRESS
    USER = bindings.v1GetExperimentsRequestSortBy.USER
    NAME = bindings.v1GetExperimentsRequestSortBy.NAME
    FORKED_FROM = bindings.v1GetExperimentsRequestSortBy.FORKED_FROM
    RESOURCE_POOL = bindings.v1GetExperimentsRequestSortBy.RESOURCE_POOL
    PROJECT_ID = bindings.v1GetExperimentsRequestSortBy.PROJECT_ID
    CHECKPOINT_SIZE = bindings.v1GetExperimentsRequestSortBy.CHECKPOINT_SIZE
    CHECKPOINT_COUNT = bindings.v1GetExperimentsRequestSortBy.CHECKPOINT_COUNT
    SEARCHER_METRIC_VAL = bindings.v1GetExperimentsRequestSortBy.SEARCHER_METRIC_VAL

    def _to_bindings(self) -> bindings.v1GetExperimentsRequestSortBy:
        return bindings.v1GetExperimentsRequestSortBy(self.value)


class ExperimentOrderBy(enum.Enum):
    """Specifies whether a sorted list of experiments should be in ascending or
    descending order.

    This class is deprecated in favor of ``OrderBy`` and will be removed in a future
    release.
    """

    def __getattribute__(self, name: str) -> Any:
        warnings.warn(
            "'ExperimentOrderBy' is deprecated and will be removed in a future "
            "release. Please use 'experimental.OrderBy' instead.",
            FutureWarning,
            stacklevel=1,
        )
        return super().__getattribute__(name)

    ASCENDING = bindings.v1OrderBy.ASC.value
    DESCENDING = bindings.v1OrderBy.DESC.value

    def _to_bindings(self) -> bindings.v1OrderBy:
        return bindings.v1OrderBy(self.value)


class Experiment:
    """A class representing an Experiment object.

    An Experiment object is usually obtained from
    :func:`determined.experimental.client.create_experiment`
    or :func:`determined.experimental.client.get_experiment` and contains helper methods
    that support querying the set of checkpoints associated with an experiment.

    Attributes:
        id: ID of experiment object in database.
        session: HTTP request session.
        config: (Mutable, Optional[Dict]) Experiment config for the experiment.
        state: (Mutable, Optional[experimentv1State) State of the experiment.
        archived: (Mutable, bool) True if experiment is archived, else false.
        name: (Mutable, str) Human-friendly name of the experiment.
        progress: (Mutable, float) Completion progress of experiment in range (0, 1.0) where 1.0
            is 100% completion.
        description: (Mutable, string) Description of the experiment.
        notes: (Mutable, str) Notes for the experiment.
        labels: (Mutable, Optional[List]) Labels associated with the experiment.
        project_id: (Mutable, int) The ID of the project associated with the experiment.
        workspace_id: (Mutable, int) The ID of the workspace associated with the experiment.

    Note:
        All attributes are cached by default.

        Some attributes are mutable and may be changed by methods that update these values,
        either automatically (eg. :meth:`wait()`) or explicitly with :meth:`reload()`.
    """

    def __init__(
        self,
        experiment_id: int,
        session: api.Session,
    ):
        self._id = experiment_id
        self._session = session

        # These properties may be mutable and will be set by _hydrate()
        self.config: Optional[Dict[str, Any]] = None
        self.state: Optional[ExperimentState] = None
        self.labels: Optional[Set[str]] = None
        self.archived: Optional[bool] = None
        self.name: Optional[str] = None
        self.progress: Optional[float] = None
        self.description: Optional[str] = None
        self.notes: Optional[str] = None
        self.project_id: Optional[int] = None
        self.workspace_id: Optional[int] = None

    @property
    def id(self) -> int:
        return self._id

    def _hydrate(self, exp: bindings.v1Experiment) -> None:
        self.config = exp.config
        self.state = ExperimentState(exp.state.value)
        self.archived = exp.archived
        self.name = exp.name
        self.progress = exp.progress
        self.description = exp.description
        self.notes = exp.notes
        self.labels = set(exp.labels) if exp.labels else None
        self.project_id = exp.projectId
        self.workspace_id = exp.workspaceId

    def reload(self) -> None:
        """
        Explicit refresh of cached properties.
        """
        resp = bindings.get_GetExperiment(self._session, experimentId=self.id).experiment
        self._hydrate(resp)

    def set_name(self, name: str) -> None:
        """Set (overwrite if existing) name on the experiment."""
        req_body = bindings.v1PatchExperiment(id=self.id, name=name)
        resp = bindings.patch_PatchExperiment(self._session, experiment_id=self.id, body=req_body)
        self.name = resp.experiment.name if resp.experiment else None

    def set_description(self, description: str) -> None:
        """Set description (overwrite if existing) description on the experiment."""
        req_body = bindings.v1PatchExperiment(id=self.id, description=description)
        resp = bindings.patch_PatchExperiment(self._session, experiment_id=self.id, body=req_body)
        self.description = resp.experiment.description if resp.experiment else None

    def set_notes(self, notes: str) -> None:
        """Set notes (overwrite if existing) description on the experiment."""
        req_body = bindings.v1PatchExperiment(id=self.id, notes=notes)
        resp = bindings.patch_PatchExperiment(self._session, experiment_id=self.id, body=req_body)
        self.notes = resp.experiment.notes if resp.experiment else None

    def add_label(self, label: str) -> None:
        """Add a label to the experiment.

        Makes a PUT request to the master and sets ``self.labels`` to the server's updated
            labels.

        Arguments:
            label: a string label to add to the experiment. If the label already exists,
                the method call will be a no-op.
        """

        resp = bindings.put_PutExperimentLabel(
            session=self._session, experimentId=self.id, label=label
        )
        self.labels = set(resp.labels)

    def remove_label(self, label: str) -> None:
        """Removes a label from the experiment.

        Makes a DELETE request to the master and sets ``self.labels`` to the server's updated
            labels.

        Arguments:
            label: a string label to remove from the experiment. If the specified label does not
                exist on the experiment, this method call will be a no-op.
        """

        resp = bindings.delete_DeleteExperimentLabel(
            session=self._session, experimentId=self.id, label=label
        )
        self.labels = set(resp.labels)

    def set_labels(self, labels: Set[str]) -> None:
        """Sets experiment labels to the given set.

        This method makes a PATCH request to the master and sets ``self.labels`` to the server's
            response. This will overwrite any existing labels on the experiment with the specified
            labels.

        Arguments:
            labels: a set of string labels to set on the experiment.
        """
        patch_exp = bindings.v1PatchExperiment(id=self.id, labels=list(labels))
        resp = bindings.patch_PatchExperiment(self._session, body=patch_exp, experiment_id=self.id)
        assert resp.experiment
        self.labels = set(resp.experiment.labels) if resp.experiment.labels else None

    def activate(self) -> None:
        bindings.post_ActivateExperiment(self._session, id=self._id)

    def archive(self) -> None:
        bindings.post_ArchiveExperiment(self._session, id=self._id)
        self.archived = True

    def cancel(self) -> None:
        bindings.post_CancelExperiment(self._session, id=self._id)

    def delete(self) -> None:
        """
        Delete an experiment and all its artifacts from persistent storage.

        You must be authenticated as admin to delete an experiment.
        """
        bindings.delete_DeleteExperiment(self._session, experimentId=self._id)

    def download_code(self, output_dir: Optional[str] = None) -> str:
        """Downloads a zipped tarball (``*.tar.gz``) of the experiment's submitted code locally.

        Saves a file named ``exp-{ID}_model_def.tar.gz`` to a local output directory. If a file
        with the same name already exists in the output directory, overwrites the file.

        Arguments:
            output_dir (string, optional): The local directory path to save downloaded archive to,
                creating directory if it does not exist. If unspecified, will save to current
                working directory.

        Returns:
             Filepath of downloaded code archive.
        """
        resp = bindings.get_GetModelDef(self._session, experimentId=self._id)
        output_filename = f"exp-{self.id}_model_def.tar.gz"
        if output_dir:
            # Expand "~" to user home directory path.
            output_path = pathlib.Path(output_dir).expanduser()
            output_path.mkdir(parents=True, exist_ok=True)
            output_path = output_path / output_filename
        else:
            output_path = pathlib.Path(output_filename)

        with output_path.open("wb") as f:
            f.write(base64.b64decode(resp.b64Tgz))

        return str(output_path)

    def get_trials(
        self,
        sort_by: trial.TrialSortBy = trial.TrialSortBy.ID,
        order_by: OrderBy = OrderBy.ASCENDING,
    ) -> List[trial.Trial]:
        warnings.warn(
            "Experiment.get_trials() has been deprecated and will be removed in a future version."
            "Please call Experiment.list_trials() instead.",
            FutureWarning,
            stacklevel=2,
        )
        return self.list_trials(sort_by, order_by)

    def list_trials(
        self,
        sort_by: trial.TrialSortBy = trial.TrialSortBy.ID,
        order_by: OrderBy = OrderBy.ASCENDING,
    ) -> List[trial.Trial]:
        """Fetch all trials of an experiment.

        Arguments:
            sort_by: Which field to sort by. See :class:`~determined.experimental.TrialSortBy`.
            order_by: Whether to sort in ascending or descending order. See
                :class:`~determined.experimental.TrialOrderBy`.
        """
        return list(self.iter_trials(sort_by, order_by))

    def iter_trials(
        self,
        sort_by: trial.TrialSortBy = trial.TrialSortBy.ID,
        order_by: OrderBy = OrderBy.ASCENDING,
        limit: Optional[int] = None,
    ) -> Iterator[trial.Trial]:
        """Generate an iterator of trials of an experiment.

        Arguments:
            sort_by: Which field to sort by. See :class:`~determined.experimental.TrialSortBy`.
            order_by: Whether to sort in ascending or descending order. See
                :class:`~determined.experimental.OrderBy`.
            limit: Optional field that sets maximum page size of the response from the server.
                When there are many trials to return, a lower page size can result in shorter
                latency at the expense of more HTTP requests to the server. Defaults to no maximum.

        Returns:
            This method returns an Iterable of :class:`~determined.experimental.Trial` instances
            that lazily fetches response objects.
        """

        def get_with_offset(offset: int) -> bindings.v1GetExperimentTrialsResponse:
            return bindings.get_GetExperimentTrials(
                self._session,
                experimentId=self._id,
                offset=offset,
                orderBy=bindings.v1OrderBy(order_by.value),
                limit=limit,
                sortBy=bindings.v1GetExperimentTrialsRequestSortBy(sort_by.value),
            )

        resps = api.read_paginated(get_with_offset)

        for r in resps:
            for t in r.trials:
                yield trial.Trial._from_bindings(t, self._session)

    def await_first_trial(self, interval: float = 0.1) -> trial.Trial:
        """
        Wait for the first trial to be started for this experiment.
        """
        while True:
            resp = bindings.get_GetExperimentTrials(
                self._session,
                experimentId=self._id,
                orderBy=bindings.v1OrderBy.ASC,
                sortBy=bindings.v1GetExperimentTrialsRequestSortBy.START_TIME,
            )
            if len(resp.trials) > 0:
                return trial.Trial._from_bindings(resp.trials[0], self._session)
            time.sleep(interval)

    def kill(self) -> None:
        bindings.post_KillExperiment(self._session, id=self._id)

    def pause(self) -> None:
        bindings.post_PauseExperiment(self._session, id=self._id)

    def unarchive(self) -> None:
        bindings.post_UnarchiveExperiment(self._session, id=self._id)
        self.archived = False

    def move_to_project(self, workspace_name: str, project_name: str) -> None:
        """Move an experiment to a different project.

        Updates both the local object and the master database with the new project and workspace.

        Args:
            project_name: The name of the destination project for the experiment.
            workspace_name: The name of the workspace containing the project.
        """
        proj = workspace.Workspace(
            session=self._session, workspace_name=workspace_name
        ).get_project(project_name)

        req = bindings.v1MoveExperimentRequest(experimentId=self._id, destinationProjectId=proj.id)
        bindings.post_MoveExperiment(self._session, body=req, experimentId=self._id)

        self.project_id = proj.id
        self.workspace_id = proj.workspace_id

    def wait(self, interval: float = 5.0) -> ExperimentState:
        """
        Wait for the experiment to reach a complete or terminal state.

        Arguments:
            interval (int, optional): An interval time in seconds before checking
                next experiment state.
        """
        elapsed_time = 0.0
        while True:
            self.reload()
            if self.state in (
                ExperimentState.COMPLETED,
                ExperimentState.CANCELED,
                ExperimentState.DELETED,
                ExperimentState.ERROR,
            ):
                return self.state
            elif self.state == ExperimentState.PAUSED:
                raise ValueError(
                    f"Experiment {self.id} is in paused state. Make sure the experiment is active."
                )
            else:
                # ACTIVE, STOPPING_COMPLETED, etc.
                time.sleep(interval)
                elapsed_time += interval
                if elapsed_time % 60 == 0:
                    print(
                        f"Waiting for Experiment {self.id} to complete. "
                        f"Elapsed {elapsed_time / 60} minutes",
                        file=sys.stderr,
                    )

    def top_checkpoint(
        self,
        sort_by: Optional[str] = None,
        smaller_is_better: Optional[bool] = None,
    ) -> checkpoint.Checkpoint:
        """
        Return the :class:`~determined.experimental.Checkpoint` for this experiment that
        has the best validation metric, as defined by the ``sort_by`` and ``smaller_is_better``
        arguments.

        Arguments:
            sort_by (string, optional): The name of the validation metric to
                order checkpoints by. If this parameter is not specified, the metric
                defined in the experiment configuration ``searcher`` field will be used.

            smaller_is_better (bool, optional): Specifies whether to sort the
                metric above in ascending or descending order. If ``sort_by`` is unset,
                this parameter is ignored. By default, the value of ``smaller_is_better``
                from the experiment's configuration is used.
        """
        warnings.warn(
            "Experiment.top_checkpoint() has been deprecated and will be removed in a future "
            "version."
            "Please call Experiment.list_checkpoints(...,max_results=1) instead.",
            FutureWarning,
            stacklevel=2,
        )
        order_by = None
        if sort_by:
            order_by = OrderBy.ASC if smaller_is_better else OrderBy.DESC
        checkpoints = self.list_checkpoints(
            sort_by=sort_by,
            order_by=order_by,
            max_results=1,
        )

        if not checkpoints:
            raise AssertionError("No checkpoints found for experiment {}".format(self.id))

        return checkpoints[0]

    def list_checkpoints(
        self,
        sort_by: Optional[Union[str, checkpoint.CheckpointSortBy]] = None,
        order_by: Optional[OrderBy] = None,
        max_results: Optional[int] = None,
    ) -> List[checkpoint.Checkpoint]:
        """Returns a list of sorted :class:`~determined.experimental.Checkpoint` instances.

        Requires either both `sort_by` and `order_by` to be defined, or neither. If neither are
        specified, will default to sorting by the experiment's configured searcher metric, and
        ordering by `smaller_is_better`.

        Only checkpoints in a ``COMPLETED`` state with a matching ``COMPLETED`` validation
        are considered.

        Arguments:
            sort_by: (Optional) Parameter to sort checkpoints by. Accepts either
                ``checkpoint.CheckpointSortBy`` or a string representing a validation metric name.
            order_by: (Optional) Order of sorted checkpoints (ascending or descending).
            max_results: (Optional) Maximum number of results to return. Defaults to no maximum.

        Returns:
            A list of sorted and ordered checkpoints.
        """
        if (sort_by is None) != (order_by is None):
            raise AssertionError("sort_by and order_by must be either both set, or neither.")

        if sort_by and not isinstance(sort_by, (checkpoint.CheckpointSortBy, str)):
            raise ValueError("sort_by must be of type CheckpointSortBy or str")

        if not sort_by:
            sort_by = checkpoint.CheckpointSortBy.SEARCHER_METRIC

        def get_with_offset(offset: int) -> bindings.v1GetExperimentCheckpointsResponse:
            return bindings.get_GetExperimentCheckpoints(
                self._session,
                id=self._id,
                limit=max_results,
                offset=offset,
                orderBy=order_by._to_bindings() if order_by else None,
                sortByAttr=sort_by._to_bindings()
                if isinstance(sort_by, checkpoint.CheckpointSortBy)
                else None,
                sortByMetric=sort_by if isinstance(sort_by, str) else None,
                states=[bindings.checkpointv1State.COMPLETED],
            )

        resps = api.read_paginated(
            get_with_offset=get_with_offset,
            pages=api.PageOpts.single if max_results else api.PageOpts.all,
        )

        return [
            checkpoint.Checkpoint._from_bindings(c, self._session)
            for r in resps
            for c in r.checkpoints
        ]

    def top_n_checkpoints(
        self,
        limit: int,
        sort_by: Optional[str] = None,
        smaller_is_better: Optional[bool] = None,
    ) -> List[checkpoint.Checkpoint]:
        """
        Return the N :class:`~determined.experimental.Checkpoint` instances with the best
        validation metrics, as defined by the ``sort_by`` and ``smaller_is_better``
        arguments. This method will return the best checkpoint from the
        top N best-performing distinct trials of the experiment. Only checkpoints in
        a ``COMPLETED`` state with a matching ``COMPLETED`` validation are considered.

        Arguments:
            limit (int): The maximum number of checkpoints to return.

            sort_by (string, optional): The name of the validation metric to use for
                sorting checkpoints. If this parameter is unset, the metric defined
                in the experiment configuration searcher field will be
                used.

            smaller_is_better (bool, optional): Specifies whether to sort the
                metric above in ascending or descending order. If ``sort_by`` is unset,
                this parameter is ignored. By default, the value of ``smaller_is_better``
                from the experiment's configuration is used.
        """
        warnings.warn(
            "Experiment.top_n_checkpoints() has been deprecated and will be removed in a future "
            "version."
            "Please call Experiment.list_checkpoints(...,max_results=n) instead.",
            FutureWarning,
            stacklevel=2,
        )

        def get_with_offset(offset: int) -> bindings.v1GetExperimentCheckpointsResponse:
            return bindings.get_GetExperimentCheckpoints(
                self._session,
                id=self._id,
                offset=offset,
                states=[bindings.checkpointv1State.COMPLETED],
            )

        resps = api.read_paginated(get_with_offset)

        checkpoints = [
            checkpoint.Checkpoint._from_bindings(c, self._session)
            for r in resps
            for c in r.checkpoints
        ]

        if not checkpoints:
            raise AssertionError("No checkpoint found for experiment {}".format(self.id))

        if not sort_by:
            training = checkpoints[0].training
            assert training
            config = training.experiment_config
            sb = config.get("searcher", {}).get("metric")
            if not isinstance(sb, str):
                raise ValueError(
                    "no searcher.metric found in experiment config; please provide a sort_by metric"
                )
            sort_by = sb
            smaller_is_better = config.get("searcher", {}).get("smaller_is_better", True)

        reverse = not smaller_is_better

        def key(ckpt: checkpoint.Checkpoint) -> Any:
            training = ckpt.training
            assert training
            metric = training.validation_metrics.get("avgMetrics") or {}
            metric = metric.get(sort_by)

            # Return a tuple that ensures checkpoints missing metrics appear last.
            if reverse:
                return metric is not None, metric
            else:
                return metric is None, metric

        checkpoints.sort(reverse=not smaller_is_better, key=key)

        # Ensure returned checkpoints are from distinct trials.
        t_ids = set()
        checkpoint_refs = []
        for ckpt in checkpoints:
            training = ckpt.training
            assert training
            if training.trial_id not in t_ids:
                checkpoint_refs.append(ckpt)
                t_ids.add(training.trial_id)

        return checkpoint_refs[:limit]

    def delete_tensorboard_files(self) -> None:
        """Delete tensorboard files for this experiment.

        This will remove the directory:
            /<root>/tensorboard/experiment/<id>
        from
            /<root>/tensorboard/experiment

        for the id of this experiment.
        """
        bindings.delete_DeleteTensorboardFiles(
            self._session,
            experimentId=self._id,
        )

    def __repr__(self) -> str:
        return "Experiment(id={})".format(self.id)

    @classmethod
    def _from_bindings(
        cls, exp_bindings: bindings.v1Experiment, session: api.Session
    ) -> "Experiment":
        exp = cls(session=session, experiment_id=exp_bindings.id)
        exp._hydrate(exp_bindings)
        return exp


class ExperimentReference(Experiment):
    """A legacy class representing an Experiment object.

    This class was renamed to :class:`~determined.experimental.Experiment` and will be removed
    in a future release.
    """

    def __init__(
        self,
        experiment_id: int,
        session: api.Session,
    ):
        warnings.warn(
            "'ExperimentReference' was renamed to 'Experiment' and will be removed in a future "
            "release. Please replace all code references to 'ExperimentReference' "
            "with 'Experiment'.",
            FutureWarning,
            stacklevel=2,
        )
        Experiment.__init__(self, experiment_id=experiment_id, session=session)
