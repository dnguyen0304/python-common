# -*- coding: utf-8 -*-

import io
import uuid

from nose.tools import assert_equal, raises, assert_true

from common import repositories


class Lines:

    def __init__(self, data):
        self.lines_uuid = str(uuid.uuid4())
        self.data = data

    def __repr__(self):
        repr_ = '{}(data="{}")'
        return repr_.format(self.__class__.__name__, self.data)


class FileDBContext(repositories.BaseDBContext):
    pass


class FileRepository(repositories.BaseRepository):
    pass


class TestFileRepository:

    def __init__(self):
        self.db_context = FileDBContext()
        self.repository = FileRepository(db_context=self.db_context)
        self.line = Lines(data='foo')

    def test_get(self):
        results = self.help_test_add(with_explicit_commit=True)
        assert_true(all(isinstance(result, Lines) for result in results))

    @raises(repositories.NoResultsFound)
    def test_get_no_results_found(self):
        self.repository.get().filter(lines_uuid=str(uuid.uuid4()).execute()

    def test_add_with_explicit_commit(self):
        results = self.help_test_add(with_explicit_commit=True)
        assert_equal(results[0].lines_uuid, self.line.lines_uuid)

    def test_add_without_explicit_commit(self):
        results = self.help_test_add(with_explicit_commit=False)
        assert_equal(results[0].lines_uuid, self.line.lines_uuid)

    def help_test_add(self, with_explicit_commit):
        try:
            self.repository.get().filter(data='foo').execute()
        except repositories.NoResultsFound:
            pass

        self.repository.add(entity=self.line)
        if with_explicit_commit:
            self.db_context.commit()
        results = self.repository.get().filter(data='foo').execute()

        return results
