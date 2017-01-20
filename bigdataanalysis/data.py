import pandas as pd
import pickle

reader = pd.read_csv('data1.txt',header=None,dtype=None,encoding='utf-8-sig',iterator=True)
keys = [20170110,20170109,20170108,20170107]
d = {}
try:
    data = reader.get_chunk(20000000)
    groupby = data.groupby([1])
    for key in keys:
    	five_date_before_id = []
    	for i in range(1,6):
    		five_date_before_id = five_date_before_id+groupby.groups[key-i]
    	d[key] = list(set(groupby.groups[key]).difference(set(five_date_before_id)))
    output = open('myfile.pkl', 'wb')
    pickle.dump(d, output)
    output.close()

    # read pickle
    # pkl_file = open('myfile.pkl', 'rb')
    # mydict2 = pickle.load(pkl_file)
    # pkl_file.close()
except StopIteration:
    print "Iteration is stopped."
