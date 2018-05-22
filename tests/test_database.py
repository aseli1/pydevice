from dm_requests import DeviceMagic
from .test_object import test_object
import vcr
 
dm = test_object

@vcr.use_cassette('fixtures/cassettes/database/without_params')
def test_without_params():
	response = dm.database.json()
	assert isinstance(response, dict)

@vcr.use_cassette('fixtures/cassettes/database/with_params')
def test_with_params():
	response = dm.database.json("from_date=2016-12-1 00:00", "to_date=2017-1-30 00:00")
	assert isinstance(response, dict)
	assert response['current_count'], 12

