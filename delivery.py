import os
import numpy as np


def load_image_names(main_path):
    img_names = os.listdir(main_path)
    img_names.sort()    
    return np.array(img_names)
            
def data_delivery(main_path,
                  path_attr=None,
                  need_id=False,
                  need_parts=False,
                  need_attr=True):
    '''
    
    Parameters
    ----------
    main_path : TYPE string
        DESCRIPTION. the path of images folder
    path_attr : TYPE numpy array
        DESCRIPTION.
    need_parts : TYPE true/false
        DESCRIPTION. The default is False.
        if it is false returns a tuple containes a list of 
        image_names and their attributes in numpy and a list of ids  
    need_attr : when we want to see the whole attributes as a target vector 
    Returns
    -------
    '''
    
    output = {}
    attr_vec = np.load(path_attr) # numpy array
    if need_attr: output.update({'attributes':attr_vec[:,:-1]})
    
    if need_id: 
        output.update({'id':attr_vec[:,-1]})        
    img_names = load_image_names(main_path)
    output.update({'img_names':img_names,
                    'id':np.array([int(i.split('_')[0]) for i in img_names]),
                    'cam_id':np.array([int(i.split('_')[1][1]) for i in img_names])})
    if need_parts:  
        output.update({'gender':attr_vec[:,0].reshape(len(attr_vec), 1),
                    'head':attr_vec[:,1:6],
                    'head_colour':attr_vec[:,6].reshape(len(attr_vec), 1),
                    'body':attr_vec[:,7:10],
                    'body_type':attr_vec[:,10].reshape(len(attr_vec), 1),
                    'body_colour':attr_vec[:,11:19],
                    'bags':attr_vec[:,19:22],
                    'leg':attr_vec[:,22:25],
                    'leg_colour':attr_vec[:,25:34],
                    'foot':attr_vec[:,34:37],                       
                    'foot_colour':attr_vec[:,37:41],
                    'age':attr_vec[:,41:45]})
        
    output.update({'names' : ['gender','cap','hairless','short hair','long hair',
                              'knot', 'h_colorful/h_black','Tshirt/shirt', 'coat',
                              'top','simple/patterned','b_w','b_r',
                              'b_y','b_green','b_b',
                              'b_gray','b_p','b_black','backpack', 'bag','no bag','pants',
                              'short','skirt','l_w','l_r','l_br','l_y','l_green','l_b',
                              'l_gray','l_p','l_black','shoes','sandal',
                              'hidden','no color','f_w', 'f_colorful','f_black','young', 
                              'teenager', 'adult', 'old']})        
    return output
