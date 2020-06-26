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


@vcr.use_cassette('tests/cassettes/resource/clone_without_params')
def test_clone_without_params():
    response = dm.resource.clone(
        test_resource['update_id'],
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    filename = response['resource']['original_filename']
    description = response['resource']['description']
    assert isinstance(response, dict)
    assert filename == 'CLONE - test_resource.xlsx'
    assert description == 'CLONE - test_resource'


@vcr.use_cassette('tests/cassettes/resource/clone_with_params')
def test_clone_with_params():
    response = dm.resource.clone(
        test_resource['update_id'],
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        description='cloned_file',
        file_name='cloned_file.xlsx')
    filename = response['resource']['original_filename']
    description = response['resource']['description']
    assert isinstance(response, dict)
    assert filename == 'cloned_file.xlsx'
    assert description == 'cloned_file'


@vcr.use_cassette('tests/cassettes/resource/file_from_path_update')
def test_file_from_path_update():
    response = dm.resource.update(
        test_resource['update_id'], 'test_resource', 'test_resource.xlsx')
    assert isinstance(response, dict)


@vcr.use_cassette('tests/cassettes/resource/file_param_update')
def test_file_param_update():
    response = dm.resource.update(
        test_resource['update_id'], 'test_resource', 'test_resource.xlsx',
        test_resource['file_data'],
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    assert isinstance(response, dict)


@vcr.use_cassette('tests/cassettes/resource/delete')
def test_delete():
    response = dm.resource.delete(test_resource['delete_id'])
    assert response == 'Resource deleted'
