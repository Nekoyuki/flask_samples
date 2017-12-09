#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import restapi


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = restapi.app.test_client()

    def test_get(self):
        res = self.app.get('/')
        assert res.status_code == 404

if __name__ == '__main__':
    unittest.main()
