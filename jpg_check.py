#!/usr/bin/env python

#!/usr/bin/env python


def filecheck(*self):

  from sys import argv
  import glob
  import subprocess
  import time


  

  filename_arg0,dir_arg1 = argv


  #Aquire the name of file or files in directory

  try:

    files = (glob.glob(('%s*' % dir_arg1)))

  except:

    print("No Such path found")


  #Return values

  Error_files = []
  Detected_files = []


  #These are the magic bytes

  arr_jpg_mb = ['\xff','\xd8','\xff','\xe0']
  str_jpg_mb = ''.join(arr_jpg_mb)
  mb_len = len(str_jpg_mb)
  

  for each_file in files:


    #Batch Processing
    time.sleep(0.025)



    #Reading each file name.
    try:



      with open(each_file,"rb") as each_file_read:

        bytes = []
        
        #Reads file by 1 byte. This can be modified by read(int)
        byte = each_file_read.read(mb_len)


        while byte != "":

          bytes.append(byte)

          byte = each_file_read.read(mb_len)   #Next byte
          

        
        #If they matched the byte with magic byte list

        if(bytes[0] == str_jpg_mb):
          
          Detected_files.append(each_file)
        
          
            
            
#Create new file
#        try :
#
#          with open(("%s.jpg" % each_file),"w+") as jpg_file:  
#             
#            jpg_file.write(each_file_read.read())
#            #bytes can be modified, that's why read(1) rather than #read(). But INEFFICIENT!
#            jpg_file.close()
#
#        except IOError:
#
#          print("Couldn't create a file")
#      rf.close()



#If an error occured, creates a list for that
    except:  

      Error_files.append(each_file)

  return Detected_files


if __name__ == "__main__":
  _fileCheck = filecheck()
  for i in (_fileCheck):
    print(i)
  




