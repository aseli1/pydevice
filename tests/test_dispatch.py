from pydevice import DeviceMagic
from .test_object import test_object, test_dispatch
import vcr

dm = test_object

@vcr.use_cassette('tests/cassettes/dispatch/all')
def test_all():
    response = dm.dispatch.all()
    assert isinstance(response, str)

@vcr.use_cassette('tests/cassettes/dispatch/push')
def test_push():
    response = dm.dispatch.push(test_dispatch['push_json'])
    assert response == "Dispatch successful"

@vcr.use_cassette('tests/cassettes/dispatch/update')
def test_update():
    response = dm.dispatch.update(test_dispatch['oneshot_id'], test_dispatch['push_json'])
    assert response == "Dispatch updated"

@vcr.use_cassette('tests/cassettes/dispatch/delete')
def test_delete():
    response = dm.dispatch.delete(test_dispatch['oneshot_id'])
    assert response == "Dispatch deleted"