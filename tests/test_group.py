from pydevice import DeviceMagic
from .test_object import test_object, test_group
import vcr

dm = test_object

@vcr.use_cassette('tests/cassettes/group/all')
def test_all():
    response = dm.group.all()
    assert isinstance(response, dict)

@vcr.use_cassette('tests/cassettes/group/create')
def test_create():
    response = dm.group.create(test_group['create_json'])
    assert response == 'Group created'

@vcr.use_cassette('tests/cassettes/group/update')
def test_update():
    response = dm.group.update(test_group['update_id'], test_group['update_json'])
    assert response == 'Group updated'

@vcr.use_cassette('tests/cassettes/group/delete')
def test_delete():
    response = dm.group.delete(test_group['delete_id'])
    assert response == 'Group deleted'
