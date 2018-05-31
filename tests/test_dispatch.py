from pydevice import DeviceMagic
from .test_object import test_object, test_dispatch
import vcr

dm = test_object

@vcr.use_cassette('tests/cassettes/dispatch/all_without_device')
def test_all_without_device():
    response = dm.dispatch.all()
    assert isinstance(response, str)

@vcr.use_cassette('tests/cassettes/dispatch/all_with_device')
def test_all_with_device():
    response = dm.dispatch.all(device_identifier=test_dispatch['device_identifier'])
    assert isinstance(response, str)

@vcr.use_cassette('tests/cassettes/dispatch/push')
def test_push():
    response = dm.dispatch.push(test_dispatch['device_identifier'], test_dispatch['push_json'])
    assert response == "Dispatch successful"

@vcr.use_cassette('tests/cassettes/dispatch/update')
def test_update():
    response = dm.dispatch.update(test_dispatch['device_identifier'], test_dispatch['update_oneshot_id'], test_dispatch['push_json'])
    assert response == "Dispatch updated"

@vcr.use_cassette('tests/cassettes/dispatch/delete_with_id')
def test_delete_with_id():
    response = dm.dispatch.delete(test_dispatch['device_identifier'], oneshot_id=test_dispatch['delete_oneshot_id'])
    assert response == "Dispatch deleted"

@vcr.use_cassette('tests/cassettes/dispatch/delete_without_id')
def test_delete_without_id():
    response = dm.dispatch.delete(test_dispatch['device_identifier'])
    assert response == "Dispatch deleted"