#import os for the manipulation of files and folders
import os
#define the path where the files and folders will be created
%cd new_folder_1_changed/
#NAME FILES AND FOLDERS BASED ON THEIR NUMBER(ODD/EVEN)
def make_files_or_directories():
    dir_num=int(input('Please enter how many directories you want to create:'))
    file_num=int(input('Please enter how many text files you want to create:'))

    if dir_num>2:
        for i in range(1,dir_num+1):
            if i%2==0:
                if os.path.exists('Even-{}'.format(i)):
                    pass
                else:
                    os.mkdir('Even-{}'.format(i))
            elif i%2!=0:
                if os.path.exists('Odd-{}'.format(i)):
                    pass
                else:
                    os.mkdir('Odd-{}'.format(i))
    elif dir_num==1:
        if os.path.exists('Odd-1'):
            pass
        else:
            os.mkdir('Odd-1')
        
    elif dir_num==0:
        print('No Directories were created')
    
    
    if file_num>2:
        for i in range(1,file_num+1):
            if i%2==0:
                f=open('Even_text_file_{}.txt'.format(i),'w')
                f.write('This is an Even numbered file and an automation task')
                f.close()
            elif i%2!=0:
                f=open('Odd_text_file_{}.txt'.format(i),'w')
                f.write('This is an Odd numbered file and an automation task')
                f.close()
    elif file_num==1:
        f=open('Odd_text_file_1.txt','w')
        f.write('This is an Odd numbered file and an automation task')
        f.close()
    elif file_num==0:
        print('No files were created!!')
    
    
    
    print('Executed Successfully!')

def make_files_or_directories():
    dir_num=int(input('Please enter how many directories you want to create:'))
    file_num=int(input('Please enter how many text files you want to create:'))

    if dir_num>2:
        for i in range(1,dir_num+1):
            if i%2==0:
                if os.path.exists('Even-{}'.format(i)):
                    pass
                else:
                    os.mkdir('Even-{}'.format(i))
            elif i%2!=0:
                if os.path.exists('Odd-{}'.format(i)):
                    pass
                else:
                    os.mkdir('Odd-{}'.format(i))
    elif dir_num==1:
        if os.path.exists('Odd-1'):
            pass
        else:
            os.mkdir('Odd-1')
        
    elif dir_num==0:
        print('No Directories were created')
    
    
    if file_num>2:
        for i in range(1,file_num+1):
            if i%2==0:
                f=open('Even_text_file_{}.txt'.format(i),'w')
                f.write('This is an Even numbered file and an automation task')
                f.close()
            elif i%2!=0:
                f=open('Odd_text_file_{}.txt'.format(i),'w')
                f.write('This is an Odd numbered file and an automation task')
                f.close()
    elif file_num==1:
        f=open('Odd_text_file_1.txt','w')
        f.write('This is an Odd numbered file and an automation task')
        f.close()
    elif file_num==0:
        print('No files were created!!')
    
    
    
    print('Executed Successfully!')
# CUSTOM NAMING OF TEXT FILES AND FOLDERS
def make_files_or_directories_with_custom_name():
    dir_num=int(input('Please enter how many directories you want to create:'))
    file_num=int(input('Please enter how many text files you want to create:'))
    dir_name=input('Enter directory name:')
    file_name=input('Enter file name:')
    if dir_num>2:
        for i in range(1,dir_num+1):
            if os.path.exists('{}-{}'.format(dir_name,i)):
                pass
            else:
                if i==1:
                    os.mkdir('{}'.format(dir_name))
                elif i>1:
                    os.mkdir('{}-{}'.format(dir_name,i-1))

    elif dir_num==1:
        if os.path.exists('{}'.format(dir_name)):
            pass
        else:
            os.mkdir('{}'.format(dir_name))
        
    elif dir_num==0:
        print('No Directories were created')
    
    
    if file_num>2:
        for i in range(1,file_num+1):
            if i==1:

                f=open('{}_text_file.txt'.format(file_name),'w')
                f.write('This is a text file and an automation task')
                f.close()
            elif i>1:
                
                f=open('{}_text_file_{}.txt'.format(file_name,i-1),'w')
                f.write('This is a file and an automation task')
                f.close()

    elif file_num==1:
        
        f=open('{}_text_file.txt'.format(file_name),'w')
        f.write('This is a file and an automation task')
        f.close()
    elif file_num==0:
        print('No files were created!!')
    
    
    
    print('Executed Successfully!')
make_files_or_directories()
make_files_or_directories_with_custom_name()