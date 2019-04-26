def insertdelim(mystring, list_field_length):

    position = 0

    for each_fld_length in list_field_length:

        l = int(each_fld_length)

        yield mystring[position:position + l]

        position += l

 

def read_file_field_length(dml_file_name):

                list_field_len = []

                with open(dml_file_name,"r") as f:

                                for each_line in f:

                                                data_types,field_length,field_name=each_line.strip().split("|")

                                                list_field_len.append(int(field_length))

 

                                return list_field_len

                                #print (list_field_len)

 

 

def get_record_type(record_type):

                list_rec_type_meta_data=[]

                if record_type=="CPN":

                                v_dml_filename="Z:\\Desktop\\BACKUP3\\PYTHON\\DML_TRAVEL_AGENT_LOAD_CPN_DATA.txt"

                elif record_type=="HDR":

                                v_dml_filename="Z:\\Desktop\\BACKUP3\\PYTHON\\DML_TRAVEL_AGENT_LOAD_HDR_DATA.txt"

                elif record_type=="MIS":

                                v_dml_filename="Z:\\Desktop\\BACKUP3\\PYTHON\\DML_TRAVEL_AGENT_LOAD_MIS_DATA.txt"

                else:

                                v_dml_filename="Z:\\Desktop\\BACKUP3\\PYTHON\\DML_TRAVEL_AGENT_LOAD_TRL_DATA.txt"

                #print ("Record_Type_Found:", record_type," in ",v_dml_filename)

                list_rec_type_meta_data=read_file_field_length(v_dml_filename)

                return list_rec_type_meta_data

 

def read_travel_agent_inbnd_file ():

                DELIMITER="|"

                with open("Z:\\Desktop\\BACKUP3\\PYTHON\\Travel_Agent_File_MIS_RECORD_V2.txt") as myfile:

                                for each_line1 in myfile:

                                                v_inv_rec_type=each_line1[0:3]

                                                v_field_length=get_record_type(v_inv_rec_type)

                                                print (v_field_length)

                                                resultant_string = (list(insertdelim(each_line1, v_field_length)))

                                                myLine = DELIMITER.join(map(str, resultant_string))

                                                print (myLine)

 

read_travel_agent_inbnd_file ()