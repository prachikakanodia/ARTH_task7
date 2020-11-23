import os
import getpass

password = getpass.getpass("Password : ")

if password != "LVM" :
	print("Incorrect password")
	exit()

while True :

	os.system("clear")
		
	print("""
	\n
	Press 1 : Automation to make LVM partition
  
                1) Check Exists Harddisk
		2) Physical Volume
		3) Volume Group
		4) Logical Volume
		5) Formatting
		6) Mounting
		

	Press 2 : Exit the Program
	""")


	ch = input("Enter ur choice : ")

	if ch=="1":
		os.system("fdisk -l")
		pv1 = input("enter name/path of the disk 1 : ")
		pv2 = input("enter name/path of the disk 2 : ")
		os.system("pvcreate /dev/{}".format(pv1))
		os.system("pvcreate /dev/{}".format(pv2))
		vgname = input("enter name of ur vg : ")
		os.system("vgcreate {} /dev/{} /dev/{}".format(vgname,pv1,pv2))
		lvsize = input("enter size of ur lv : ")
		lvname = input("enter name of ur lv : ")
		os.system("lvcreate --size +{} --name {} {}".format(lvsize,lvname,vgname))
		os.system("tput setaf 3")
		print("successfully created logical volume...")
		os.system("tput setaf 7")
		os.system("lvdisplay {}/{}".format(vgname,lvname))
		input("press enter to format ur lv {}".format(lvname))
		os.system("mkfs.ext4 /dev/{}/{}".format(vgname,lvname))
		print("successfully formatted ur lv {}".format(lvname))
		fol = input("enter name of ur folder : ")
		os.system("/{}".format(fol))
		print("mounting ur lv {} to the /{} folder".format(lvname,fol))
		os.system("mount /dev/{}/{} /{}".format(vgname,lvname,fol))
		print("successfully mounted ur lv {} to /{} folder".format(lvname,fol))

	elif ch=="2":
		exit()

	else:
		print("Invalid choice")
	input()
	
