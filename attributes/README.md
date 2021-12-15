# CA_Market1501

The evaluation code will be added soon.

## About dataset
We annotate 48 attributes for [Market-1501](http://zheng-lab.cecs.anu.edu.au/Project/project_reid.html). 
The original dataset contains 751 identities for training and 750 identities for testing. 
The attributes are annotated in the image-based level on gt_bbox folder of Market-1501 dataset, 
thus the file contains a total_attr.npy file with size of 25259 x 48 which includes 48 binary attributes and two other files, train_idx.pth and test_idx.pth that are indexes of train and test images of sorted gt_bbox folder.
The size of train_idx is 12567 and the size of test_idx is 12692. 

The 48 attributes are: 

|attribute|   |part|       |column index|

 gender        gender           0
 cap           head             1
 hairless      head             2
 short hair    head             3
 long hair     head             4
 knot hair     head             5
 colorful      head color       6
 black         head color       7
 short sleeve  body             8
 long sleeve   body             9
 coat          body             10
 top           body             11
 patterned     body type        12
 white         body color       13
 red           body color       14
 yellow        body color       15
 green         body color       16
 blue          body color       17
 gray          body color       18
 purple        body color       19
 black         body color       20
 backpack      bags             21 
 shoulder bag  bags             22
 hand bag      bags             23
 no bag        bags             24
 pants         leg              25
 shorts        leg              26
 skirt         leg              27
 white         leg color        28
 red           leg color        29
 brown         leg color        30
 yellow        leg color        31
 green         leg color        32
 blue          leg color        33
 gray          leg color        34
 purple        leg color        35
 black         leg color        36
 shoes         foot             37
 sandal        foot             38
 hidden        foot             39
 no color      foot color       40
 white         foot color       41
 colorful      foot color       42
 black         foot color       43
 young         age              44
 teenager      age              45
 adult         age              46
 old           age              47
 
 
  
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
}
```
Market-1501 Dataset:
```
@inproceedings{zheng2015scalable,
  title={Scalable person re-identification: A benchmark},
  author={Zheng, Liang and Shen, Liyue and Tian, Lu and Wang, Shengjin and Wang, Jingdong and Tian, Qi},
  booktitle={Proceedings of the IEEE International Conference on Computer Vision},
  year={2015}
}
```

