"""
Simple example showing Clarifai Custom Model training and prediction

This example trains a concept classifier that recognizes photos of the band Phish.
"""

from clarifai_basic import ClarifaiCustomModel


# instantiate clarifai client
clarifai = ClarifaiCustomModel()

concept_name = 'speaker system'

# find some positive and negative examples
SPEAKERSYSTEM_POSITIVES = [
'http://www.userlib.com/wp-content/uploads/2015/07/surround-sound.jpeg',
'http://www.superfi.co.uk/images/product/large/16570_1_.jpg',
'http://scene7.targetimg1.com/is/image/Target/14450360?wid=480&hei=480',
'http://static0.bornrichimages.com/wp-content/uploads/s3/1/2012/08/01/the_aperion_wireless_home_theater_speaker_system_look_ma_no_hands_z1c12.jpg',
'http://3.bp.blogspot.com/-rDz_fTxXs0Q/Tz9ZHVT4L2I/AAAAAAAAFFo/mIhd8cFhWGo/s1600/Creative+Labs+Gigaworks+S750+7.1+Speaker+System.png'
]

# add the positive example images to the model
for positive_example in SPEAKERSYSTEM_POSITIVES:
  clarifai.positive(positive_example, concept_name)


# negatives are not required but will help if you want to discriminate between similar concepts
SPEAKERSYSTEM_NEGATIVES = [
  'http://www.zopomobileshop.com/images/Portable_Bluetooth_Mini_Speaker_3.jpg',
  'http://audiospeakerguide.com/wp-content/uploads/2014/04/beats_pill_portable_bluetooth_speaker.jpg',
  'http://www.blogcdn.com/www.engadget.com/media/2010/11/jawbone-jambox-11-17-2010.jpg',
  'http://core0.staticworld.net/images/idge/imported/article/ctw/2012/08/24/bts_hmdxjam_338-100393573-orig.jpg',
  'http://a.tgcdn.net/images/products/zoom/eec0_x-mini_kai_bluetooth_speaker.jpg'
  ]
# add the negative example images to the model
for negative_example in SPEAKERSYSTEM_NEGATIVES:
  clarifai.negative(negative_example, concept_name)

# train the model
clarifai.train(concept_name)


SPEAKERSYSTEM_EXAMPLES = [
  'http://www.userlib.com/wp-content/uploads/2015/07/surround-sound.jpeg',
'http://www.superfi.co.uk/images/product/large/16570_1_.jpg',
]

NOT_SPEAKERSYSTEM= [
  'http://core0.staticworld.net/images/idge/imported/article/ctw/2012/08/24/bts_hmdxjam_338-100393573-orig.jpg',
  'http://a.tgcdn.net/images/products/zoom/eec0_x-mini_kai_bluetooth_speaker.jpg'
]

# If everything works correctly, the confidence that true positive images are of Phish should be
# significantly greater than 0.5, which is the same as choosing at random. The confidence that true
# negative images are Phish should be significantly less than 0.5.

# use the model to predict whether the test images are Phish or not
for test in SPEAKERSYSTEM_EXAMPLES + NOT_SPEAKERSYSTEM:
  result = clarifai.predict(test, concept_name)
  print (result['status']['message'], "%0.3f" % result['urls'][0]['score'], result['urls'][0]['url'])

# Our output is the following. Your results will vary as there are some non-deterministic elements
# of the algorithms used.

# Success 0.797 http://phishthoughts.com/wp-content/uploads/2012/07/photo-1-11-e1342391144673.jpg
# Success 0.706 http://bobmarley.cdn.junip.com/wp-content/uploads/2014/10/DSC01226-e1311293061704.jpg
# Success 0.356 http://farm3.static.flickr.com/2161/2141620332_2b741028b3.jpg
# Success 0.273 http://www.mediaspin.com/joel/grateful_dead230582_15-52.jpg

concept_name = 'vacuum'

# find some positive and negative examples
VACUUM_POSITIVES = [
'http://www.electroluxgroup.com/en/wp-content/uploads/sites/2/2012/04/Electrolux-Ergorapido-Antique-Steel.jpg',
'http://ecx.images-amazon.com/images/I/3173ZKc56qL._SY300_.jpg',
'http://newsroom.electrolux.com/uk/wp-content/common/photos_uk/electrolux-2012-02-15-ergobrushclean-closeup-aeg.jpg',
'http://img1.lesnumeriques.com/produits/22/11117/ergorapido-coloris(1).jpg',
'http://1.im6.fr/03E8000000601790-c2-photo-aspirateur-electrolux-ergorapido-2007-zb-2811-clone.jpg'
  
]

# add the positive example images to the model
for positive_example in VACUUM_POSITIVES:
  clarifai.positive(positive_example, concept_name)


# negatives are not required but will help if you want to discriminate between similar concepts
VACUUM_NEGATIVES = [
  'http://contentinjection.com/wp-content/uploads/2013/09/lightweight-vacuum-cleaners-for-home-and-car-usage.jpg',
  'https://cdn.tutsplus.com/vector/uploads/legacy/tuts/000-2012/496-vacuum-cleaner/0.jpg',
  'http://www.vacmag.com/wp-content/uploads/2013/09/bagless.jpg',
  'http://contentinjection.com/wp-content/uploads/2013/09/lightweight-vacuum-cleaners-for-home-and-car-usage.jpg',
  'http://www.homegear1.com/images/Roomba560Reviews.jpg'
  ]
# add the negative example images to the model
for negative_example in VACUUM_NEGATIVES:
  clarifai.negative(negative_example, concept_name)

# train the model
clarifai.train(concept_name)


VACUUM_EXAMPLES = [
  'http://img1.lesnumeriques.com/produits/22/11117/ergorapido-coloris(1).jpg',
'http://1.im6.fr/03E8000000601790-c2-photo-aspirateur-electrolux-ergorapido-2007-zb-2811-clone.jpg'
]

NOT_VACUUM= [
  'http://contentinjection.com/wp-content/uploads/2013/09/lightweight-vacuum-cleaners-for-home-and-car-usage.jpg',
  'http://www.homegear1.com/images/Roomba560Reviews.jpg'
]

# If everything works correctly, the confidence that true positive images are of Phish should be
# significantly greater than 0.5, which is the same as choosing at random. The confidence that true
# negative images are Phish should be significantly less than 0.5.

# use the model to predict whether the test images are Phish or not
for test in VACUUM_EXAMPLES + NOT_VACUUM:
  result = clarifai.predict(test, concept_name)
  print (result['status']['message'], "%0.3f" % result['urls'][0]['score'], result['urls'][0]['url'])

#new concept sleeping bag 
  concept_name = 'sleeping bag'

# find some positive and negative examples
SLEEPINGBAG_POSITIVES = [
'http://www.everythingsummercamp.com/common/images/products/large/exxel-outdoors-colorado-adult-sleeping-bag.jpg',
'http://i1.adis.ws/i/jpl/bl_113133_a',
'http://hybris.webcity.com.au/~pur17863/wp-content/uploads/2009/02/p1000377_1-300x288.jpg',
'http://www.everythingsummercamp.com/common/images/products/large/sleeping-bag-suisse-sport-everest.jpg',
'http://www.trespass.com/media/catalog/product/e/c/echotec-blue-2.jpg'

]

# add the positive example images to the model
for positive_example in SLEEPINGBAG_POSITIVES:
  clarifai.positive(positive_example, concept_name)


# negatives are not required but will help if you want to discriminate between similar concepts
SLEEPINGBAG_NEGATIVES = [
  'http://www.beyondblackwhite.com/wp-content/uploads/2015/07/14Fa0223_HR300-resize.jpg',
  'http://ec1.ostkcdn.com/images/products/6620948/Bedford-Black-Queen-Bed-P14188276.jpg',
  'https://www.stlbeds.com/wp-content/uploads/2014/07/bunk-bed-mission-honey-bk100-mattress_xxl.jpg',
  'http://sleep-paralysis-info.com/wp-content/uploads/2014/11/sleeping-baby.jpg',
  'https://upload.wikimedia.org/wikipedia/commons/b/b5/Sleep_woman.jpg'
  ]
# add the negative example images to the model
for negative_example in SLEEPINGBAG_NEGATIVES:
  clarifai.negative(negative_example, concept_name)

# train the model
clarifai.train(concept_name)


SLEEPINGBAG_EXAMPLES = [
'http://www.everythingsummercamp.com/common/images/products/large/exxel-outdoors-colorado-adult-sleeping-bag.jpg',
'http://i1.adis.ws/i/jpl/bl_113133_a'
]

NOT_SLEEPINGBAG= [
  'http://www.beyondblackwhite.com/wp-content/uploads/2015/07/14Fa0223_HR300-resize.jpg',
  'http://ec1.ostkcdn.com/images/products/6620948/Bedford-Black-Queen-Bed-P14188276.jpg'
]

# If everything works correctly, the confidence that true positive images are of Phish should be
# significantly greater than 0.5, which is the same as choosing at random. The confidence that true
# negative images are Phish should be significantly less than 0.5.

# use the model to predict whether the test images are Phish or not
for test in SLEEPINGBAG_EXAMPLES + NOT_SLEEPINGBAG:
  result = clarifai.predict(test, concept_name)
  print (result['status']['message'], "%0.3f" % result['urls'][0]['score'], result['urls'][0]['url'])