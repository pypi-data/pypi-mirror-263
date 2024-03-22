#=============================================================#
###  CREATED AT     : 12 MARET 2024                         ###
###  UPDATED AT     : 14 MARET 2024                         ###
###  COPYRIGHT      : BRIBRAIN DATA ENGINEER TEAM           ###
###  DESCRIPTION    : Module untuk kumpulan function        ###
#=============================================================#

from time import time
from pytz import timezone
from datetime import datetime, timedelta
from pyspark.sql import functions as F
from Crypto.Cipher import AES


import base64
import hashlib

#=============================================================#
def try_or(func, default=None, expected_exc=(Exception,)):
  """Menangkap error dan memberikan keluaran sesuai parameter

  Args:
      func (function): python function
        (notes is ditambahkan lambda pada sebelum nama function, ex: try_or(lambda:func))
      default (object): keluaran yang diharapkan ketika terjadi error
      expected_exc (Exception): Exception yang diharapkan
    
  Returns:
      object: keluaran dari function atau mengembalikan keluaran sesuai input jika terdapat error
  """
  
  try:
    return func()
  except expected_exc:
    return default
  
#=============================================================#    
def set_timer():
  """Menetapkan waktu awal untuk penghitungan durasi proses

  Args:
      -
    
  Returns:
      float: waktu dalam format float
  """
    
  global START_TIME
  START_TIME = time()
  
  return START_TIME

#=============================================================#
def get_timer(start_time=None):
  """Memperoleh durasi proses berdasarkan waktu awal dikurangi waktu sekarang

  Args:
      start_time (float) : 
    
  Returns:
      string: durasi proses dengan format HH:MM:SS
  """
    
  if start_time:
    return (datetime(1,1,1)+timedelta(seconds=int(time()-start_time))).strftime("%H:%M:%S")
  
  return (datetime(1,1,1)+timedelta(seconds=int(time()-START_TIME))).strftime("%H:%M:%S")

#=============================================================#  
def get_list_partition(spark, schema, table):
  """Memperoleh list partisi dari hive table yang diurutkan dari partisi terbaru

  Args:
      spark (pyspark.sql.session.SparkSession): spark session
      schema (str): nama schema dari table di hive
      table (str): nama table di hive
    
  Returns:
      list: list partisi diurutkan dari partisi yang terbaru
  """
  
  try:
    partitions = spark.sql("""
     SHOW PARTITIONS {}.{}
     """.format(schema, table)).sort("partition", ascending=False).collect() # ambil partisi sesuai format
    if len(partitions) != 0: # jika ada partisi
      list_partition = []
      for row in partitions:
        if "__HIVE_DEFAULT_PARTITION__" not in row[0]:
          arrange = []
          dict_partition = {}
          for partition in row[0].split("/"):
            value = partition.split("=")
            arrange.append(value[1].zfill(2))
            dict_partition[value[0]] = value[1]
          dict_partition["__formatted_partition"] = "|".join(arrange)
          list_partition.append(dict_partition)
      list_partition = sorted(list_partition, key=lambda row: row['__formatted_partition'], reverse=True)
      return list_partition
    else: # selain itu
      return None # tidak ada partisi
  except:
    print("is not a partitioned table")
    return None
  
#=============================================================#
def get_first_partition(spark, schema, table):
  """Memperoleh partisi pertama dari hive table

  Args:
      spark (pyspark.sql.session.SparkSession): spark session
      schema (str): nama schema dari table di hive
      table (str): nama table di hive
    
  Returns:
      dict: partisi pertama
  """
    
  partitions = get_list_partition(spark, schema, table)
  if partitions == None:
    return None
  
  return partitions[-1]

#=============================================================#  
def get_last_partition(spark, schema, table):
  """Memperoleh partisi terakhir dari hive table

  Args:
      spark (pyspark.sql.session.SparkSession): spark session
      schema (str): nama schema dari table di hive
      table (str): nama table di hive
    
  Returns:
      dict: partisi terakhir
  """
    
  partitions = get_list_partition(spark, schema, table)
  if partitions == None:
    return None
  
  return partitions[0]

#=============================================================#  
def get_padding(raw):
  """Menambahkan padding pada string input untuk memenuhi AES Block Size
  
  Args:
      raw (str): string input yang akan di beri padding
      
  Returns:
      str: hasil pemberian padding
  """
  
  BLOCK_SIZE = AES.block_size
  
  return raw + (BLOCK_SIZE - len(raw) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(raw) % BLOCK_SIZE)

#=============================================================#
def get_unpadding(pad):
  """Menghilangkan padding pada string input
  
  Args:
      raw (str): string input yang akan dihilangkan padding-nya
      
  Returns:
      str: hasil penghilangan padding
  """
    
  return pad[:-ord(pad[len(pad) - 1:])]
  
#=============================================================#
def get_encrypt_aes256(raw, password):
  """Melakukan enkripsi pada string input menggunakan metode AES 256 pycrypto library
  
  Args:
      raw (str): string input yang akan di enkripsi
      password (str): key yang nantinya untuk proses dekripsi
      
  Returns:
      str: hasil proses enkripsi
  """
  
  raw = get_padding(raw)

  iv_original = b"SECRET"
  iv = hashlib.sha256(iv_original).digest()[:16]

  private_key = hashlib.sha256(password.encode("utf-8")).digest()

  cipher = AES.new(private_key, AES.MODE_CBC, iv)
  ciphertext = cipher.encrypt(raw)

  encrypted_data = iv + ciphertext

  return base64.b64encode(encrypted_data).decode('utf-8')

udf_encrypt_aes256 = F.udf(lambda col1,col2: try_or(lambda: get_encrypt_aes256(col1,col2)))

#=============================================================#
def get_decrypt_aes256(enc, password):
  """Melakukan dekripsi pada string input hasil enkripsi menggunakan metode AES 256 pycrypto library
  
  Args:
      raw (str): string input yang akan di dekripsi
      password (str): key untuk proses dekripsi
      
  Returns:
      str: hasil proses dekripsi
  """
  
  private_key = hashlib.sha256(password.encode("utf-8")).digest()
  enc = base64.b64decode(enc)
  iv = enc[:16]
  cipher = AES.new(private_key, AES.MODE_CBC, iv)
  return bytes.decode(get_unpadding(cipher.decrypt(enc[16:])))

udf_decrypt_aes256 = F.udf(lambda col1,col2: try_or(lambda: get_decrypt_aes256(col1,col2)))

#=============================================================#


