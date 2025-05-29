import webbrowser
from tkinter import *
import tkinter
from tkinter import StringVar
from tkinter import ttk

aval_religion_list = ["hinduism" , "christian","islam" , "sikhism" , "buddhism" ,"judaism"]
aval_christ_script = ["Holy Bible","Apocrypha / Deuterocanonical Books","Confessions by St. Augustine","Summa Theologica by St. Thomas Aquinas","The Imitation of Christ by Thomas à Kempis","The Pilgrim’s Progress by John Bunyan","Philokalia - Vol 1","Philokalia - Vol 2","Philokalia - Vol 3","Philokalia - Vol 4","Philokalia - Vol 5","Catechism of the Catholic Church","Book of Common Prayer","The Didache"]
aval_hindu_script = ["Bhagavad Gita","Ramayana","Mahabharata","AtharvaVed - part 1","AtharvaVed - part 2","Rigveda","Samved","Yajurved","Bhagavata Purana","Shiva Purana","Upanishads","Manusmriti","Yoga Sutras of Patanjali"]
aval_islam_script = ["Quran","Sahih al-Bukhari","Sahih Muslim","Riyad as-Salihin (by Imam an-Nawawi)","40 Hadith Nawawi (by Imam an-Nawawi)","Sunan Abu Dawood","Jami` at-Tirmidhi","Tafsir Ibn Kathir","Hisnul Muslim (Fortress of the Muslim)","Muwatta Malik (by Imam Malik)"]
aval_sikh_script = ["Guru Granth Sahib","Dasam Granth","Sarbloh Granth","Rehat Maryada"]
aval_bhuddism_script = ["Tipitaka (Pali Canon)","Dhammapada","Sutta Pitaka","Vinaya Pitaka","Abhidhamma Pitaka","Lotus Sutra","Heart Sutra (Prajñāpāramitā Hridaya)","Diamond Sutra (Vajracchedikā)","Lankavatara Sutra","Tibetan Book of the Dead (Bardo Thodol)"]
aval_judiasm_script = ["Tanakh (Hebrew Bible)","Torah (Five Books of Moses)","Talmud","Mishnah","Gemara","Midrash","Siddur","Halakhah","Zohar","Haggadah"]


root = Tk()
root.title("Holy codes")
frame = tkinter.Frame(root)
frame.pack(expand=True, fill='both', padx=20, pady=20)

heading1 = Label(root , text="HolyCodes, Find Your Scripture Now !" , fg="Grey" , font=("Arial Black" , 30))
heading1.pack()

seperator = Label(root , text="----------------------------------------------------------------------", font=("Arial Black" , 30))
seperator.pack(anchor='s')

label = tkinter.Label(root, text="Select relegion :", font=("Helvetica", 22))
label.pack(anchor='center', padx=20, pady=10)

selected_option = StringVar()
selected_option.set(aval_religion_list[0])  

dropdown = ttk.Combobox(root, textvariable=selected_option, values=aval_religion_list, font=("Helvetica", 14), width=20, state="readonly")
dropdown.current()   
dropdown.pack(anchor='center', padx=20, pady=10)

# Display selected option
def selected():
    if selected_option.get() == "hinduism":
        def open():
            selected_option1_1 = selected_option1.get().lower()
            if selected_option1_1 == 'ramayana':
                webbrowser.open("https://myebookarchive.wordpress.com/wp-content/uploads/2024/03/shrimad-valmiki-ramayana.pdf")

            elif selected_option1_1 == 'mahabharata':
                webbrowser.open("https://drive.google.com/file/d/1A-j7Xpvg870qJerWxFk77tPwuL8Mzq0f/view?usp=sharing")

            elif selected_option1_1 == 'bhagavad gita':
                webbrowser.open("https://yogalife.co.in/wp-content/uploads/2017/04/Bhagavad-gita-hindi.pdf")

            elif selected_option1_1 == 'rigveda':
                webbrowser.open("https://vedpuran.net/wp-content/uploads/2011/10/rigved.pdf")

            elif selected_option1_1 == 'upanishads':
                webbrowser.open("https://ia902902.us.archive.org/3/items/in.ernet.dli.2015.486022/2015.486022.108-UPNISADAYBRAMAHA.pdf")

            elif selected_option1_1 == 'bhagavata purana':
                webbrowser.open("https://vedpuran.net/wp-content/uploads/2011/10/bhagwat-puran.pdf")

            elif selected_option1_1 == 'shiva purana':
                webbrowser.open("https://vedpuran.net/wp-content/uploads/2011/10/shiv-puran.pdf")

            elif selected_option1_1 == 'samved':
                webbrowser.open("https://vedpuran.net/wp-content/uploads/2011/10/samved.pdf")

            elif selected_option1_1 == 'manusmriti':
                webbrowser.open("https://www.shdvef.com/wp-content/uploads/2020/11/%E0%A4%AE%E0%A4%A8%E0%A5%81%E0%A4%B8%E0%A5%8D%E0%A4%AE%E0%A5%83%E0%A4%A4%E0%A4%BF-%E0%A4%B8%E0%A4%AE%E0%A5%8D%E0%A4%AA%E0%A5%82%E0%A4%B0%E0%A5%8D%E0%A4%A3.pdf")

            elif selected_option1_1 == 'yoga sutras of patanjali':
                webbrowser.open("https://uou.ac.in/sites/default/files/slm/MY-201.pdf")

            elif selected_option1_1 == 'atharvaved - part 2':
                webbrowser.open("https://vedpuran.net/wp-content/uploads/2011/10/atharva-2.pdf")

            elif selected_option1_1 == 'atharvaved - part 1':
                webbrowser.open("https://vedpuran.net/wp-content/uploads/2011/10/arthved-part-1.pdf")

            elif selected_option1_1 == 'yajurved':
                webbrowser.open("https://vedpuran.net/wp-content/uploads/2011/10/yajurved.pdf")

            root.destroy()

        srpt_label = Label(root, text="Select your scripture", font=("Helvetica", 22))
        srpt_label.pack(anchor='center' , padx=20 , pady=10)
        
        selected_option1 = StringVar()
        selected_option1.set("choose here")  

        dropdown = ttk.Combobox(root, textvariable=selected_option1, values=aval_hindu_script, font=("Helvetica", 14), width=20, state="readonly")
        dropdown.current()  
        dropdown.pack(anchor='center', padx=20, pady=10)

        btn1 = tkinter.Button(root, text="OPEN !", command=open , width=10 , height=2 , font=("Arial Black" , 10))
        btn1.pack(anchor='center' ,padx=20 , pady=10)

    elif selected_option.get() == "christian":
        def open():
            selected_option1_2 = selected_option1.get().lower()
            if selected_option1_2 == 'holy bible':
                webbrowser.open("https://csbible.com/wp-content/uploads/2018/03/CSB_Pew_Bible_2nd_Printing.pdf")

            elif selected_option1_2 == 'the confessions of st. augustin':
                webbrowser.open("https://ccel.org/ccel/a/augustine/confess/cache/confess.pdf")

            elif selected_option1_2 == 'apocrypha / deuterocanonical books':
                webbrowser.open("https://www.bibleclaret.org/bibles/ccb_pdf/ot/5%20Writings/7%20Tobit%20pp%20931-941.pdf")

            elif selected_option1_2 == 'summa theologica by st. thomas aquinas':
                webbrowser.open("https://www.documentacatholicaomnia.eu/03d/1225-1274,_Thomas_Aquinas,_Summa_Theologiae_%5B1%5D,_EN.pdf")

            elif selected_option1_2 == 'the imitation of christ by thomas à kempis':
                webbrowser.open("https://sufipathoflove.com/wp-content/uploads/2019/10/the-imitation-of-christ-thomas-kempis.pdf")

            elif selected_option1_2 == 'the pilgrim’s progress by john bunyan':
                webbrowser.open("https://document.desiringgod.org/the-pilgrim-s-progress-en.pdf?ts=1446648353")

            elif selected_option1_2 == 'philokalia - vol 1':
                webbrowser.open("https://ia800306.us.archive.org/24/items/philokalia-complete-volumes1-5/The%20Philokalia%20Vol%201%20-%20G.E.H.%20Palmer%3BKallistos%20Timothy.pdf")

            elif selected_option1_2 == 'philokalia - vol 2':
                webbrowser.open("https://archive.org/download/philokalia-complete-volumes1-5/The%20Philokalia%20Vol%202%20-%20G.E.H.%20Palmer%3BKallistos%20Timothy.pdf")

            elif selected_option1_2 == 'philokalia - vol 3':
                webbrowser.open("https://archive.org/download/philokalia-complete-volumes1-5/The%20Philokalia%20Vol%203%20-%20G.E.H.%20Palmer%3B.pdf")

            elif selected_option1_2 == 'philokalia - vol 4':
                webbrowser.open("https://archive.org/download/philokalia-complete-volumes1-5/The%20Philokalia%20Vol%204%20-%20G.E.H.%20Palmer%3BKallistos%20Timothy.pdf")

            elif selected_option1_2 == 'philokalia - vol 5':
                webbrowser.open("https://archive.org/download/philokalia-complete-volumes1-5/The%20Philokalia%20Vol%205%20-%20G.E.H.%20Palmer%3B.pdf")

            elif selected_option1_2 == 'catechism of the catholic church':
                webbrowser.open("https://olmca.org/ourpages/users/evillasenor/CatechismCatholicChurch2ndEdition.pdf")

            elif selected_option1_2 == 'book of common prayer':
                webbrowser.open("https://www.churchpublishing.org/siteassets/pdf/book-of-common-prayer/book-of-common-prayer-2006.pdf")

            elif selected_option1_2 == 'the didache':
                webbrowser.open("https://legacyicons.com/content/didache.pdf")

            root.destroy()

        srpt_label = Label(root, text="Select your scripture", font=("Helvetica", 22))
        srpt_label.pack(anchor='center' , padx=20 , pady=10)
        
        selected_option1 = StringVar()
        selected_option1.set("choose here")  

        dropdown = ttk.Combobox(root, textvariable=selected_option1, values=aval_christ_script, font=("Helvetica", 14), width=20, state="readonly")
        dropdown.current()  
        dropdown.pack(anchor='center', padx=20, pady=10)

        btn1 = tkinter.Button(root, text="OPEN !", command=open , width=10 , height=2 , font=("Arial Black" , 10))
        btn1.pack(anchor='center' ,padx=20 , pady=10)
    
    elif selected_option.get() == "islam":
        def open():
            selected_option1_3 = selected_option1.get().lower()
            if selected_option1_3 == 'Quran':
                webbrowser.open("https://upload.wikimedia.org/wikipedia/commons/b/b2/The_Holy_Quran.pdf")

            elif selected_option1_3 == 'Sahih al-Bukhari':
                webbrowser.open("https://dn790009.ca.archive.org/0/items/154296/154296.pdf")

            elif selected_option1_3 == 'Sahih Muslim':
                webbrowser.open("https://ia601304.us.archive.org/0/items/sahih-muslim-arabic/sahih-muslim-arabic.pdf")

            elif selected_option1_3 == 'Riyad as-Salihin (by Imam an-Nawawi)':
                webbrowser.open("https://dn790000.ca.archive.org/0/items/Riyad-Us-Saliheen-ARABIC.pdf/Riyad-Us-Saliheen-ara.pdf")

            elif selected_option1_3 == '40 Hadith Nawawi (by Imam an-Nawawi)':
                webbrowser.open("https://ia801307.us.archive.org/17/items/40HadithOfImamNawawi/40%20Hadith%20of%20Imam%20Nawawi.pdf")

            elif selected_option1_3 == 'Sunan Abu Dawood':
                webbrowser.open("https://dn790008.ca.archive.org/0/items/sunanabidawoodarabic/Sunan%20Abi%20Dawood-%20Arabic.pdf")

            elif selected_option1_3 == 'Jami` at-Tirmidhi':
                webbrowser.open("https://dn790007.ca.archive.org/0/items/sunantirmiziarabic/Sunan%20Tirmizi-%20Arabic.pdf")

            elif selected_option1_3 == 'Tafsir Ibn Kathir':
                webbrowser.open("https://dn790006.ca.archive.org/0/items/TafseerAlQuranAlAzeemTafseerIbneKaseerArabic/Tafseer%20Al-Quran%20Al-Azeem%20-%20Tafseer%20ibne%20Kaseer%20%28Arabic%20%29.pdf")

            elif selected_option1_3 == 'Hisnul Muslim (Fortress of the Muslim)':
                webbrowser.open("https://mjc.org.za/wp-content/uploads/2018/11/HISN-AL-MUSLIM-FORTRESS-OF-THE-MUSLIM.pdf")

            elif selected_option1_3 == 'Muwatta Malik (by Imam Malik)':
                webbrowser.open("https://ia802901.us.archive.org/32/items/20200328_20200328_0428/%D8%A7%D9%84%D9%85%D8%A4%D8%B7%D8%A7%20%D8%A7%D9%85%D8%A7%D9%85%20%D9%85%D8%A7%D9%84%DA%A9%20%D8%A8%D9%86%20%D8%A7%D9%86%D8%B3.pdf")

            root.destroy()

        srpt_label = Label(root, text="Select your scripture", font=("Helvetica", 22))
        srpt_label.pack(anchor='center' , padx=20 , pady=10)
        
        selected_option1 = StringVar()
        selected_option1.set("choose here")  

        dropdown = ttk.Combobox(root, textvariable=selected_option1, values=aval_islam_script, font=("Helvetica", 14), width=20, state="readonly")
        dropdown.current()  
        dropdown.pack(anchor='center', padx=20, pady=10)

        btn1 = tkinter.Button(root, text="OPEN !", command=open , width=10 , height=2 , font=("Arial Black" , 10))
        btn1.pack(anchor='center' ,padx=20 , pady=10)        

    elif selected_option.get() == "sikhism":
        def open():
            selected_option1_4 = selected_option1.get().lower()
            if selected_option1_4 == 'guru granth sahib':
                webbrowser.open("https://www.sikhnet.com/files/ereader/SGGS%20%5BGurmukhi%5D.pdf")

            elif selected_option1_4 == 'dasam granth':
                webbrowser.open("https://ia601601.us.archive.org/12/items/DasamGranthAll/Dasam%20Granth_All.pdf")

            elif selected_option1_4 == 'sarbloh granth':
                webbrowser.open("https://media.sikher.com/files/Complete-Sri-Sarbloh-Granth-Sahib-Ji-Steek.pdf")

            elif selected_option1_4 == 'rehat maryada':
                webbrowser.open("https://www.dsgmc.in/Files/Rehat-Maryada-_Punjabi_.pdf")

            root.destroy()

        srpt_label = Label(root, text="Select your scripture", font=("Helvetica", 22))
        srpt_label.pack(anchor='center' , padx=20 , pady=10)
        
        selected_option1 = StringVar()
        selected_option1.set("choose here")  

        dropdown = ttk.Combobox(root, textvariable=selected_option1, values=aval_sikh_script, font=("Helvetica", 14), width=20, state="readonly")
        dropdown.current()  
        dropdown.pack(anchor='center', padx=20, pady=10)

        btn1 = tkinter.Button(root, text="OPEN !", command=open , width=10 , height=2 , font=("Arial Black" , 10))
        btn1.pack(anchor='center' ,padx=20 , pady=10)

    elif selected_option.get() == "buddhism":
        def open():
            selected_option1_5 = selected_option1.get()
            if selected_option1_5 == 'Tibetan Book of the Dead (Bardo Thodol)':
                webbrowser.open("https://isharonline.org/wp-content/uploads/The-Tibetan-Book-of-the-Dead.pdf")

            elif selected_option1_5 == 'Dhammapada':
                webbrowser.open("https://www.bps.lk/olib/bp/bp203s_Buddharakkhita_Dhammapada.pdf")

            elif selected_option1_5 == 'Sutta Pitaka':
                webbrowser.open("https://www.dhammatalks.org/Archive/Writings/Ebooks/SuttaPitaka210710.pdf")

            elif selected_option1_5 == 'Vinaya Pitaka':
                webbrowser.open("https://svakhum.wordpress.com/wp-content/uploads/2011/02/vinaya-pitaka-1.pdf")

            elif selected_option1_5 == 'Abhidhamma Pitaka':
                webbrowser.open("https://patthana.net/wp-content/uploads/2017/03/Puggalapannatti_Mn.pdf")

            elif selected_option1_5 == 'Lotus Sutra':
                webbrowser.open("https://www.bdk.or.jp/document/dgtl-dl/dBET_T0262_LotusSutra_2007.pdf")

            elif selected_option1_5 == 'Heart Sutra (Prajñāpāramitā Hridaya)':
                webbrowser.open("https://www.buddhanet.net/pdf_file/heart_s2.pdf")

            elif selected_option1_5 == 'Diamond Sutra (Vajracchedikā)':
                webbrowser.open("https://www.lifelonglearningcollaborative.org/silkroads/articles/diamond-sutra-translation.pdf")

            elif selected_option1_5 == 'Lankavatara Sutra':
                webbrowser.open("https://www.ebharatisampat.in/pdfs/1711012467.pdf")

            root.destroy()

        srpt_label = Label(root, text="Select your scripture", font=("Helvetica", 22))
        srpt_label.pack(anchor='center' , padx=20 , pady=10)
        
        selected_option1 = StringVar()
        selected_option1.set("choose here")  

        dropdown = ttk.Combobox(root, textvariable=selected_option1, values=aval_bhuddism_script, font=("Helvetica", 14), width=20, state="readonly")
        dropdown.current()  
        dropdown.pack(anchor='center', padx=20, pady=10)

        btn1 = tkinter.Button(root, text="OPEN !", command=open , width=10 , height=2 , font=("Arial Black" , 10))
        btn1.pack(anchor='center' ,padx=20 , pady=10)
        
    elif selected_option.get() == "judaism":
        def open():
            selected_option1_6 = selected_option1.get().lower()
            if selected_option1_6 == 'Tanakh (Hebrew Bible)':
                webbrowser.open("https://ferrusca.wordpress.com/wp-content/uploads/2016/11/thetanakh.pdf")

            elif selected_option1_6 == 'Torah (Five Books of Moses)':
                webbrowser.open("https://www.betemunah.org/Torah.pdf")

            elif selected_option1_6 == 'Talmud':
                webbrowser.open("https://www.jewishvirtuallibrary.org/jsource/Judaism/FullTalmud.pdf")

            elif selected_option1_6 == 'Mishnah':
                webbrowser.open("https://www.islamforchristians.com/wp-content/uploads/2014/09/Mishnah-in-English-by-Danby.pdf")

            elif selected_option1_6 == 'Midrash':
                webbrowser.open("https://www.friendsofsabbath.org/Further_Research/Godhead/THE%20MIDRASH%20OF%20THE%20MESSIAH.pdf")

            elif selected_option1_6 == 'Siddur':
                webbrowser.open("https://cbbsb.org/wp-content/uploads/2020/03/Mashiv-Haruach-CBB-Siddur-text.pdf")

            elif selected_option1_6 == 'Halakhah':
                webbrowser.open("https://www.practicalhalacha.com/book.pdf")

            elif selected_option1_6 == 'Zohar':
                webbrowser.open("https://www.calledoutbelievers.org/wp-content/uploads/2018/09/The_Book_of_Zohar-Introduction.pdf")

            elif selected_option1_6 == 'Haggadah':
                webbrowser.open("https://w2.chabad.org/media/pdf/1125/rCjo11252600.pdf")


            root.destroy()

        srpt_label = Label(root, text="Select your scripture", font=("Helvetica", 22))
        srpt_label.pack(anchor='center' , padx=20 , pady=10)
        
        selected_option1 = StringVar()
        selected_option1.set("choose here")  

        dropdown = ttk.Combobox(root, textvariable=selected_option1, values=aval_judiasm_script, font=("Helvetica", 14), width=20, state="readonly")
        dropdown.current()  
        dropdown.pack(anchor='center', padx=20, pady=10)

        btn1 = tkinter.Button(root, text="OPEN !", command=open , width=10 , height=2 , font=("Arial Black" , 10))
        btn1.pack(anchor='center' ,padx=20 , pady=10)

btn = tkinter.Button(root, text="Select !", command=selected , width=10 , height=2 , font=("Arial Black" , 10))
btn.pack(anchor='center' ,padx=20 , pady=10)

seperator1 = Label(root , text="----------------------------------------------------------------------", font=("Arial Black" , 30))
seperator1.pack(anchor='s')

root.mainloop()




    
