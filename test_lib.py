from lib import moyenne

def test_moyenne():
	data =[1,1,1]

	result = moyenne(data)


	assert result == 1

if __name__ == '__main__':
	test_moyenne()