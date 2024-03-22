import base64

import pytest

from upsies import utils
from upsies.trackers import base
from upsies.trackers.ant import AntTrackerConfig


@pytest.fixture
def tracker_config():
    return AntTrackerConfig()


def test_AntTrackerConfig_defaults(tracker_config):
    assert set(tracker_config) == {
        'base_url',
        'apikey',
        'announce_url',
        'source',
        'exclude',
        'anonymous',

        # Inherited from TrackerConfigBase
        'add_to',
        'copy_to',
        'randomize_infohash',
    }


def test_AntTrackerConfig_defaults_base_url(tracker_config):
    assert tracker_config['base_url'] == base64.b64decode('aHR0cHM6Ly9hbnRoZWxpb24ubWU=').decode('ascii')


def test_AntTrackerConfig_defaults_username(tracker_config):
    assert tracker_config['apikey'] == ''
    assert tracker_config['apikey'].description == (
        'Your person upload API key you created in your profile.'
    )


def test_AntTrackerConfig_defaults_announce_url(tracker_config):
    assert tracker_config['announce_url'] == ''
    assert tracker_config['announce_url'].description == (
        'Your personal announce URL.'
    )


def test_AntTrackerConfig_defaults_source(tracker_config):
    assert tracker_config['source'] == 'ANT'


def test_AntTrackerConfig_defaults_exclude(tracker_config):
    assert tracker_config['exclude'] == (
        utils.types.RegEx(base.exclude.checksums),
        utils.types.RegEx(base.exclude.images),
        utils.types.RegEx(base.exclude.nfo),
        utils.types.RegEx(base.exclude.samples),
    )


def test_AntTrackerConfig_defaults_anonymous(tracker_config):
    assert isinstance(tracker_config['anonymous'], utils.types.Bool)
    assert not tracker_config['anonymous']
    assert tracker_config['anonymous'] == 'no'
    assert tracker_config['anonymous'].description == (
        'Whether your username is displayed on your uploads.'
    )


def test_AntTrackerConfig_arguments(tracker_config):
    exp_argument_definitions = {
        'submit': {
            ('--anonymous', '--an'),
        },
    }
    assert set(tracker_config.argument_definitions) == set(exp_argument_definitions)
    for command in exp_argument_definitions:
        assert set(tracker_config.argument_definitions[command]) == exp_argument_definitions[command]


def test_AntTrackerConfig_argument_definitions_submit_anonymous(tracker_config):
    assert tracker_config.argument_definitions['submit'][('--anonymous', '--an')] == {
        'help': 'Hide your username for this submission',
        'action': 'store_true',
        'default': None,
    }
