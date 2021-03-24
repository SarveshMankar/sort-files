import os
import shutil
#Part 1, Check and Make the required Folders
a=os.listdir('.')
b='.'
lst=[]
for i in a:
	if b in i:
		lst.append(i)
extensions=[]
for i in lst:
	b=i.split('.')
	extensions.append(str('.')+str(b[int(len(b))-1]).lower())

print("Extensions",extensions)

if '.png' or '.jpeg' or '.jpg' or '.tiff' in extensions:
	try:
		os.mkdir("Photos")
	except:
		pass
if '.css' or '.py' or '.java' or '.php' or '.html' or '.c' or '.cpp' or '.ipynb' or '.less' or '.asm' or '.json' or '.joblib' or '.js' in extensions:
	try:
		os.mkdir("Programming")
	except:
		pass
if '.odt' or '.docx' or '.doc' or '.txt' or '.pdf' or '.wpd' or '.rtf' or '.ods' or '.odp' or '.ppt' or '.pptx' or '.url' in extensions:
	try:
		os.mkdir("Text")
	except:
		pass
if '.mp3' or '.aac' or '.wav' or '.flac' or '.ram' or '.wma' or '.mpa' or '.ra' in extensions:
	try:
		os.mkdir("Music")
	except:
		pass
if '.mp4' or '.webm' or '.gif' or '.m4p' or '.mp2' or '.mov' in extensions:
	try:
		os.mkdir("Videos")
	except:
		pass
if '.csv' or '.db' or '.psql' or '.data' or '.xlsx' in extensions:
	try:
		os.mkdir("Data_Sets")
	except:
		pass
if '.zip' or '.deb' or '.rpm' or '.gz' or '.tar' or '.xz' or '.rar' or '.arj' or '.sit' or '.sitx' or '.7z' or '.tar.xz' or '.exe' or '.msi' in extensions:
	try:
		os.mkdir("Compressed_and_Installer")
	except:
		pass
if '.torrent' in extensions:
	try:
		os.mkdir("Torrent_Files")
	except:
		pass

if '.apk' in extensions:
	try:
		os.mkdir("Mobile Apps")
	except:
		pass
	
#Part 2, Sorting all the files into appropriate Folders.
for i in lst:
	#Photos
	if i[-4:]=='.png' or i[-4:]=='.jpg' or i[-5:]=='.tiff':
		try:
			shutil.move(str(i),"Photos")
		except:
			pass
	if i[-5:]=='.jpeg':
		try:
			shutil.move(str(i),"Photos")
		except:
			pass
	#Executable
	if i[-4:]=='.exe' or i[-4:]=='.msi':
		try:
			shutil.move(str(i),"Compressed_and_Installer")
		except:
			pass
	#Data Sets
	if i[-4:]=='.csv' or i[-3:]=='.db' or i[-5:]=='.psql' or i[-5:]=='.data' or i[-5:]=='.xlsx':
		try:
			shutil.move(str(i),"Data_Sets")
		except:
			pass
	#Programs
	if i[-4:]=='.css' or i[-3:]=='.py' or i[-5:]=='.java' or i[-4:]=='.php' or i[-5:]=='.html' or i[-2:]=='.c' or i[-4:]=='.cpp' or i[-6:]=='.ipynb' or i[-5:]=='.less' or i[-4:]=='.asm' or i[-5:]=='.json' or i[-7:]=='.joblib' or i[-3:]=='.js':
		try:
			shutil.move(str(i),"Programming")
		except:
			pass
	#Text Files
	if i[-4:]=='.odt' or i[-4:]=='.doc' or i[-5:]=='.docx' or i[-4:]=='.txt' or i[-4:]=='.pdf' or i[-4:]=='.rtf' or i[-4:]=='.wpd' or i[-4:]=='.ods' or i[-4:]=='.odp' or i[-4:]=='.ppt' or i[-5:]=='.pptx' or i[-4:]=='.url':
		try:
			shutil.move(str(i),"Text")
		except:
			pass
	#Video
	if i[-4:]=='.mp4' or i[-4:]=='.gif' or i[-5:]=='.webm' or i[-4:]=='.m4p' or i[-4:]=='.mp2' or i[-4:]=='.mov':
		try:
			shutil.move(str(i),"Videos")
		except:
			pass
	#Music
	if i[-4:]=='.mp3' or i[-4:]=='.acc' or i[-4:]=='.wav' or i[-5:]=='.flac' or i[-4:]=='.ram' or i[-4:]=='.mpa' or i[-4:]=='.wma' or i[-3:]=='.ra':
		try:
			shutil.move(str(i),"Music")
		except:
			pass
	#Compress
	if i[-4:]=='.zip' or i[-4:]=='.deb' or i[-4:]=='.rpm' or i[-4:]=='.tar' or i[-3:]=='.gz' or i[-4:]=='.jar' or i[-3:]=='.xz' or i[-4:]=='.rar' or i[-4:]=='.arj' or i[-4:]=='.sit' or i[-4:]=='.sitx' or i[-3:]=='.7z' or i[-7:]=='.tar.xz':
		try:
			shutil.move(str(i),"Compressed_and_Installer")
		except:
			pass	
	#Torrent
	if i[-8:]=='.torrent':
		try:
			shutil.move(str(i),"Torrent_Files")
		except:
			pass
	#Mobile App
	if i[-4:]=='.apk':
		try:
			shutil.move(str(i),"Mobile Apps")
		except:
			pass