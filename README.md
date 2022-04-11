# CA_Market1501 

Here is the official repository for CA_Market1501 attribute dataset. You can find more details on [CA-Market: A Partially Categorical AnnotatingApproach Based on Market1501 Dataset for Attribute Detection](10.1109/ICSPIS54653.2021.9729331)

## About dataset
We have annotate 45 attributes for [Market-1501](http://zheng-lab.cecs.anu.edu.au/Project/project_reid.html). 
The original dataset contains 751 identities for training and 750 identities for testing. 
The attributes are annotated in the image-based level on gt_bbox folder of Market-1501 dataset, 
thus the file contains a CA_Market_with_id.npy
 file with size of 25259 x 46 which includes 45 binary attributes of train and test images of sorted gt_bbox folder from Market-1501 dataset and their id.
The size of train_idx is 12567 and the size of test_idx is 12692. 


The 48 attributes are: 

| attribute | part | column index |
| :----: | :----: | :----: |
 gender | gender |  0
 cap | head | 1 |
 hairless   |   head      |       2|
 short hair |   head       |      3|
 long hair  |   head    |         4|
 knot hair   |  head          |   5|
 head (colorful1, black0)  |    head color    |   6|
 Tshirt/shirt | body | 7|
 coat       |   body     |        8|
 top         |  body             9|
 patterned  |   body type   |     10|
 white      |    body color   |    11|
 red        |   body color   |    12|
 yellow     |   body color   |    13|
 green      |   body color   |    14|
 blue       |   body color   |    15|
 gray       |   body color   |    16|
 purple     |   body color   |    17|
 black      |   body color   |   18|
 backpack   |   bags         |    19 |
 bag        |   bags         |    20|
 no bag    |    bags         |    21|
 pants     |    leg          |    22|
 shorts    |    leg          |    23|
 skirt     |    leg          |    24|
 white     |    leg color    |    25|
 red       |     leg color    |    26|
 brown     |    leg color    |    27|
 yellow    |    leg color    |    28|
 green     |    leg color    |    29|
 blue      |    leg color    |    30|
 gray      |     leg color    |    31|
 purple    |    leg color    |   32|
 black     |    leg color    |    33|
 shoes     |    foot         |    34|
 sandal    |    foot         |    35|
 hidden    |    foot         |    36|
 no color  |    foot color   |    37|
 white     |    foot color   |    38|
 colorful  |    foot color   |    39|
 black     |    foot color   |    40|
 young     |    age          |    41|
 teenager  |    age          |    42|
 adult     |    age          |    43|
 old       |    age          |    44|
 id        |    id           |    45| 
  
attr_names = ['gender','cap','hairless','short hair','long hair',
           'knot', 'h_colorful', 'h_black','Tshirt_shs', 'shirt_ls','coat',
           'top','simple/patterned','b_w','b_r',
           'b_y','b_green','b_b',
           'b_gray','b_p','b_black','backpack', 'shoulder bag',
           'hand bag','no bag','pants',
           'short','skirt','l_w','l_r','l_br','l_y','l_green','l_b',
           'l_gray','l_p','l_black','shoes','sandal',
           'hidden','no color','f_w', 'f_colorful','f_black', 'young', 
           'teenager', 'adult', 'old']
## Citation

If you use this dataset in your research, please kindly cite our work as,
```
@article{
CA-Market: A Partially Categorical AnnotatingApproach Based on Market1501 Dataset for Attribute Detection
}
```
CA_Market1501 Dataset:
```
@inproceedings{bodaghi2021market,
  title={CA-Market: A Partially Categorical AnnotatingApproach Based on Market1501 Dataset for Attribute Detection},
  author={Bodaghi, Hossein and Samiee, Shayan and Masoulehe, Mehdi Tale and Kalhor, Ahmad},
  booktitle={2021 7th International Conference on Signal Processing and Intelligent Systems (ICSPIS)},
  pages={01--08},
  year={2021},
  organization={IEEE}
}
```

