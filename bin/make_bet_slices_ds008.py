#!/usr/bin/python 

subj_id = 2

#Read the file 

html_text=open('/home/kconst/Projects/local/share/templates/html/bet_slices.html')

#print(html_text.format(subj_id))

for line in html_text:
        line.find('{:03d}'),
        print (line.format(subj_id))


html_text = "\n".join(html_text)
#print(html_text.format(subj_id))

#print text into sub002_bet_slices.html
 
new_html=open('/home/kconst/Projects/output/html/sub002_bet_slices.html','w')
new_html.write(html_text.format(subj_id))
new_html.close()

