# # import pyarrow as pa
# # import pyarrow.fs as fs
# #
# # #при нестандартных форматах (мешанина)
# # hdfs = fs.HadoopFileSystem(
# #     host="test.host",
# #     port=8000,
# #     user="hadoop"
# # )
# #
# # with hdfs.open:
#
#
# def change_data(self, sql, args=None):
#     conn = self.hiveConIns()
#     cur = conn.cursor()
#     try:
#         if isinstance(args, list):
#             cur.executemany(sql, args)
#         else:
#             cur.execute(sql, args)
#         conn.commit()
#     except Exception as e:
#         print(e)
#     finally:
#         cur.close()
#         conn.close()
#
#


import pyhs2
import happybase
from constants import USER_HADOOP, PASSWORD_HADOOP, PORT_HADOOP, HOST_HADOOP

connection = happybase.Connection('bigdatalite')
test_table = connection.table('test')
b = test_table.batch(batch_size=10000)


def upload(data):
    print("sending to hadoop")
    for i in data:
        b.put(str(i[0]), {'ID_NAME': i[1],
                          'dims:name': i[2],
                          'dims:password': i[3],
                          'dims:info': i[4]})


b.send()

with pyhs2.connect(host=HOST_HADOOP,
                   port=PORT_HADOOP,
                   authMechanism="PLAIN",
                   user=USER_HADOOP,
                   password=PASSWORD_HADOOP,
                   database='default') as conn:
    if __name__ == '__main__':
        upload()
