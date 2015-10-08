#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import sys
import os.path
import urllib2


 


#カテゴリ合算、創作、ファンアート、殿堂入り
rank_url = ["http://seiga.nicovideo.jp/illust/ranking/point/daily/common","http://seiga.nicovideo.jp/illust/ranking/point/daily/g_creation","http://seiga.nicovideo.jp/illust/ranking/point/hourly/g_fanart","http://seiga.nicovideo.jp/illust/ranking/point/hourly/g_popular"]
rank_name = ["カテゴリ合算","創作","ファンアート","殿堂入り"]
base_url = "http://seiga.nicovideo.jp"
img_url = "http://lohas.nicoseiga.jp/img/"
opener = urllib2.build_opener()
tag_count = 0

print "--------  ようこそ「fav静」へ  -----------"
print "デイリーランキングから指定したタグのついた画像を自動的に保存してくれます"
print "今いるディレクトリに"
print "ランキング→タグ名→作者→画像"
print "とファイルが作られます"
print "----------------------------------------"

#入力
print "どのランキングを調べたいか番号で入力してください"
for i,rank in enumerate(rank_name):
	print str(i)+"："+rank

target_rank_num = raw_input()
target_rank = rank_url[int(target_rank_num)]

if os.path.isdir("./"+rank_name[int(target_rank_num)]) is False:
	os.mkdir(rank_name[int(target_rank_num)])
html = opener.open(target_rank).read()



print "選択したランキング："+rank_name[int(target_rank_num)]
print "検索したいタグを入力"

target_tag = raw_input()
if os.path.isdir("./"+rank_name[int(target_rank_num)]+"/"+target_tag) is False:
	os.mkdir(rank_name[int(target_rank_num)]+"/"+target_tag)

name_pat = re.compile('http://seiga\.nicovideo\.jp/seiga/im+[0-9]+')
id_tag = name_pat.findall(html)

print "------検索中------"


for ç
	#1~100
	if i > 100:
		break

	opener = urllib2.build_opener()
	page_url = opener.open(name).read()

	if target_tag in page_url:

		tag_pat = re.compile(r'class=\"tag\".*')
		name_target = re.compile(r'<strong>(.+?)<\/strong>')
		title_target = re.compile(r'<div class=\"lg_ttl_illust\"><h1>(.+?)<\/h1><\/div>')
		number_split = name.split("im")

		title = title_target.search(page_url)
		title = title.group(1)
		writer = name_target.search(page_url)
		writer = writer.group(1)
		tags = tag_pat.findall(page_url)
		for tag_name in tags:
			if target_tag in tag_name:
				print "----------------------------"
				print title
				print writer+"さんが新しく書いています"
				if os.path.isdir("./"+rank_name[int(target_rank_num)]+"/"+target_tag+"/"+writer) is False:
					os.mkdir(rank_name[int(target_rank_num)]+"/"+target_tag+"/"+writer)

				img_file = open("./"+rank_name[int(target_rank_num)]+"/"+target_tag+"/"+writer+"/"+number_split[1]+"_"+title+".png","wb")
				img = opener.open(img_url+str(number_split[1]+"l")).read()
				img_file.write(img)
				img_file.close()
				tag_count+=1
				break

print "------------------------"
print "殿堂入り毎時ランキングで"
print "タグ"+target_tag+"が"
print str(tag_count)+"件ありました"
print "------------------------"

if tag_count == 0:
	print "--------------------------------"
	print "世の中は非情だ！！！！！！！！！！！"
	print "--------------------------------"
	
