from .test_object import test_object, test_destination
import vcr

dm = test_object


@vcr.use_cassette('tests/cassettes/destination/all')
def test_all():
    response = dm.destination.all()
    assert isinstance(response, dict)


@vcr.use_cassette('tests/cassettes/destination/details')
def test_details():
    response = dm.destination.details(test_destination['details_id'])
    assert isinstance(response, dict)


@vcr.use_cassette('tests/cassettes/destination/create_without_form_id')
def test_create_without_form_id():
    response = dm.destination.create(test_destination['create_json'])
    assert isinstance(response, dict)

@vcr.use_cassette('tests/cassettes/destination/create_with_form_id')
def test_create_with_form_id():
    response = dm.destination.create(test_destination['create_json'],
                                     test_destination['form_id'])
    assert isinstance(response, dict)


@vcr.use_cassette('tests/cassettes/destination/update')
def test_update():
    response = dm.destination.update(
        test_destination['update_id'], test_destination['update_json'])
    assert isinstance(response, dict)


@vcr.use_cassette('tests/cassettes/destination/delete')
def test_delete():
    response = dm.destination.delete(test_destination['delete_id'])
    assert response == "Destination deleted"


@vcr.use_cassette('tests/cassettes/destination/copy')
def test_copy():
    response = dm.destination.copy(test_destination['copy_id'])
    assert isinstance(response, dict)
