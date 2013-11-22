new_data_file = open('data/moredata.tsv', 'w')
new_data_file.write('user_id\tarticle_id\trevision_id\tnamespace\ttimestamp\n') # header

from datetime import datetime
raw_data_file = open('data/moredata_raw.tsv')
for line in raw_data_file:
    attr = line.strip().split('\t')
    user = int(attr[0])
    article = int(attr[1])
    revision = int(attr[2])
    namespace = int(attr[3])
    timestamp_dt = datetime.strptime(attr[4], '%Y-%m-%dT%H:%M:%SZ')
    timestamp_str = timestamp_dt.strftime('%Y-%m-%d %H:%M:%S')
    new_data_file.write('%d\t%d\t%d\t%d\t%s\n' % (user, article, revision, namespace, timestamp_str))
raw_data_file.close()

new_data_file.close()
