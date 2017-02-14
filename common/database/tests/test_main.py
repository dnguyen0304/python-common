# -*- coding: utf-8 -*-

from nose.tools import assert_is_not_none, assert_true, raises

from common.database.main import DBContext


class MockModel:

    def __init__(self):
        self.created_at = None
        self.created_by = 0
        self.updated_at = None
        self.updated_by = 0


class MockEntityState:

    def __init__(self, is_transient, is_persistent):
        self.transient = is_transient
        self.persistent = is_persistent


class TestDBContext:

    def _set_up(self, is_transient, is_persistent, by=None):
        self.entity = MockModel()
        entity_state = MockEntityState(is_transient=is_transient,
                                       is_persistent=is_persistent)

        DBContext._validate_metadata(entity=self.entity,
                                     entity_state=entity_state,
                                     by=by)

    def test_validate_metadata_create_new_entity(self):
        self._set_up(is_transient=True, is_persistent=False, by=-1)
        assert_is_not_none(self.entity.created_at)
        assert_true(self.entity.created_by)

    @raises(TypeError)
    def test_validate_metadata_create_new_entity_without_specifying_by(self):
        self._set_up(is_transient=True, is_persistent=False)

    def test_validate_metadata_update_existing_entity(self):
        self._set_up(is_transient=False, is_persistent=True, by=-1)
        assert_is_not_none(self.entity.updated_at)
        assert_true(self.entity.updated_by)

    @raises(TypeError)
    def test_validate_metadata_update_existing_entity_without_specifying_by(self):
        self._set_up(is_transient=False, is_persistent=True)

