#!/usr/bin/env python
# -*- coding: utf8 -*-

#   Copyright 2013 Nikolay Spiridonov
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


import random
import time

class LuhnUUID(object):
    """ Simple UUID (16 len) generator based on Luhn algorithm and unix timestamp"""


    def __init__(self, UUID=None):
        self.UUID = UUID
        self.checksum = None

    def digits_of(self, n):
        return [int(_) for _ in str(n)]


    def luhn_checksum(self, UUID):
        digits = self.digits_of(UUID)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        self.checksum = 0
        self.checksum += sum(odd_digits)
        for d in even_digits:
            self.checksum += sum(self.digits_of(d*2))
        return self.checksum % 10


    def is_uuid_valid(self, UUID):
        return self.luhn_checksum(UUID) == 0


    def calculate_uuid(self):
        self.UUID =  str(int(time.time())) + ''.join(map(
            str, [random.randint(0,9) for _ in xrange(5)]
        ))
        check_digit = self.luhn_checksum(self.UUID * 10)
        return self.UUID + str(check_digit) if check_digit == 0 else self.UUID + str(10 - check_digit)
