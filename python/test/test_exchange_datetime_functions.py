import os
import sys

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root)

# ----------------------------------------------------------------------------

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

# ----------------------------------------------------------------------------

import ccxt  # noqa: F402
from ccxt.base.decimal_to_precision import ROUND_UP, ROUND_DOWN  # noqa F401

# ----------------------------------------------------------------------------

exchange = ccxt.Exchange({
    'id': 'regirock',
})

# ----------------------------------------------------------------------------

assert exchange.iso8601(514862627000) == '1986-04-26T01:23:47.000Z'
assert exchange.iso8601(514862627559) == '1986-04-26T01:23:47.559Z'
assert exchange.iso8601(514862627062) == '1986-04-26T01:23:47.062Z'

assert exchange.iso8601(0) == '1970-01-01T00:00:00.000Z'

assert exchange.iso8601(-1) is None
assert exchange.iso8601() is None
assert exchange.iso8601(None) is None
assert exchange.iso8601('') is None
assert exchange.iso8601('a') is None
assert exchange.iso8601({}) is None

assert exchange.parse8601('1986-04-26T01:23:47.000Z') == 514862627000
assert exchange.parse8601('1986-04-26T01:23:47.559Z') == 514862627559
assert exchange.parse8601('1986-04-26T01:23:47.062Z') == 514862627062

assert exchange.parse8601('1986-04-26T01:23:47.06Z') == 514862627060
assert exchange.parse8601('1986-04-26T01:23:47.6Z') == 514862627600

assert exchange.parse8601('1977-13-13T00:00:00.000Z') is None
assert exchange.parse8601('1986-04-26T25:71:47.000Z') is None

assert exchange.parse8601('3333') is None
assert exchange.parse8601('Sr90') is None
assert exchange.parse8601('') is None
assert exchange.parse8601() is None
assert exchange.parse8601(None) is None
assert exchange.parse8601({}) is None
assert exchange.parse8601(33) is None

assert exchange.parse_date('1986-04-26 00:00:00') == 514857600000
assert exchange.parse_date('1986-04-26T01:23:47.000Z') == 514862627000
assert exchange.parse_date('1986-13-13 00:00:00') is None


assert exchange.round_timeframe('5m', exchange.parse8601('2019-08-12 13:22:08'), ROUND_DOWN) == exchange.parse8601('2019-08-12 13:20:00')
assert exchange.round_timeframe('10m', exchange.parse8601('2019-08-12 13:22:08'), ROUND_DOWN) == exchange.parse8601('2019-08-12 13:20:00')
assert exchange.round_timeframe('30m', exchange.parse8601('2019-08-12 13:22:08'), ROUND_DOWN) == exchange.parse8601('2019-08-12 13:00:00')
assert exchange.round_timeframe('1d', exchange.parse8601('2019-08-12 13:22:08'), ROUND_DOWN) == exchange.parse8601('2019-08-12 00:00:00')

assert exchange.round_timeframe('5m', exchange.parse8601('2019-08-12 13:22:08'), ROUND_UP) == exchange.parse8601('2019-08-12 13:25:00')
assert exchange.round_timeframe('10m', exchange.parse8601('2019-08-12 13:22:08'), ROUND_UP) == exchange.parse8601('2019-08-12 13:30:00')
assert exchange.round_timeframe('30m', exchange.parse8601('2019-08-12 13:22:08'), ROUND_UP) == exchange.parse8601('2019-08-12 13:30:00')
assert exchange.round_timeframe('1h', exchange.parse8601('2019-08-12 13:22:08'), ROUND_UP) == exchange.parse8601('2019-08-12 14:00:00')
assert exchange.round_timeframe('1d', exchange.parse8601('2019-08-12 13:22:08'), ROUND_UP) == exchange.parse8601('2019-08-13 00:00:00')
