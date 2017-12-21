#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import restapi


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = restapi.app.test_client()
        self.db = restapi.db.create_all()

    def test_get_root(self):
        r = self.app.get('/')
        assert r.status_code == 404

    def test_get_sqlalc(self):
        r = self.app.get('/sqlalc/')
        assert r.status_code == 200
        assert b'"r": "GET success"' in r.data

if __name__ == '__main__':
    unittest.main()
