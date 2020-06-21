from .test_object import test_object, test_resource
import vcr

dm = test_object

@vcr.use_cassette('tests/cassettes/resource/all')
def test_all():
    response = dm.resource.all()
    assert isinstance(response, dict)

@vcr.use_cassette('tests/cassettes/resource/download')
def test_download():
    response = dm.resource.download(test_resource['download_id'])
    assert isinstance(response, bytes)

@vcr.use_cassette('tests/cassettes/resource/details')
def test_details():
    response = dm.resource.details(test_resource['download_id'])
    assert isinstance(response, dict)

@vcr.use_cassette('tests/cassettes/resource/create')
def test_create():
    response = dm.resource.create('test_resource', 'test_resource.xlsx')
    assert isinstance(response, dict)

@vcr.use_cassette('tests/cassettes/resource/update')
def test_update():
    response = dm.resource.update(test_resource['update_id'],'test_resource', 'test_resource.xlsx')
    assert isinstance(response, dict)

@vcr.use_cassette('tests/cassettes/resource/delete')
def test_delete():
    response = dm.resource.delete(test_resource['delete_id'])
    assert response == 'Resource deleted'
