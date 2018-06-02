
LABEL_COLUMN = "label"

DISPLAY_ID_COLUMN = 'display_id'

AD_ID_COLUMN = 'ad_id'

IS_LEAK_COLUMN = 'is_leak'

DISPLAY_ID_AND_IS_LEAK_ENCODED_COLUMN = 'display_ad_and_is_leak'

CATEGORICAL_COLUMNS = [
 #control_columns
 'ad_id',
 'doc_id',
 'doc_event_id',
 #feature_vector_columns
 'ad_advertiser',
 'doc_ad_source_id', 
 'doc_ad_publisher_id',
 'doc_event_publisher_id',
 'doc_event_source_id',  
 'event_country',
 'event_country_state',
 'event_geo_location',
 'event_hour',
 'event_platform',
 'traffic_source']


DOC_CATEGORICAL_MULTIVALUED_COLUMNS = {
    'doc_ad_category_id': ['doc_ad_category_id_1',
                          'doc_ad_category_id_2',
                          'doc_ad_category_id_3'],
    'doc_ad_topic_id': ['doc_ad_topic_id_1',
                         'doc_ad_topic_id_2',
                         'doc_ad_topic_id_3'],
    'doc_ad_entity_id': ['doc_ad_entity_id_1', 
                         'doc_ad_entity_id_2', 
                         'doc_ad_entity_id_3', 
                         'doc_ad_entity_id_4', 
                         'doc_ad_entity_id_5', 
                         'doc_ad_entity_id_6'],
    'doc_event_category_id': ['doc_event_category_id_1',
                              'doc_event_category_id_2',
                              'doc_event_category_id_3'],
    'doc_event_topic_id': ['doc_event_topic_id_1',
                           'doc_event_topic_id_2',
                           'doc_event_topic_id_3'],
    'doc_event_entity_id': ['doc_event_entity_id_1',
                            'doc_event_entity_id_2',
                            'doc_event_entity_id_3',
                            'doc_event_entity_id_4',
                            'doc_event_entity_id_5',
                            'doc_event_entity_id_6']
}

BOOL_COLUMNS = ['event_weekend',
                      'user_has_already_viewed_doc']

INT_COLUMNS = ['user_views',
                    'ad_views',
                    'doc_views',
                    'doc_event_days_since_published',
                    'doc_event_hour',
                    'doc_ad_days_since_published']                  


FLOAT_COLUMNS_LOG_BIN_TRANSFORM = ['pop_ad_id',                                
                        'pop_ad_id_conf_multipl', 
                        'pop_document_id',                                        
                        'pop_document_id_conf_multipl',
                        'pop_publisher_id',                        
                        'pop_publisher_id_conf_multipl',
                        'pop_advertiser_id',                        
                        'pop_advertiser_id_conf_multipl',
                        'pop_campain_id',                        
                        'pop_campain_id_conf_multipl',
                        'pop_doc_event_doc_ad',                        
                        'pop_doc_event_doc_ad_conf_multipl',
                        'pop_source_id',                          
                        'pop_source_id_conf_multipl',
                        'pop_source_id_country',                        
                        'pop_source_id_country_conf_multipl',
                        'pop_entity_id',                            
                        'pop_entity_id_conf_multipl',
                        'pop_entity_id_country',                        
                        'pop_entity_id_country_conf_multipl',
                        'pop_topic_id',                         
                        'pop_topic_id_conf_multipl',
                        'pop_topic_id_country',                        
                        'pop_topic_id_country_conf_multipl',
                        'pop_category_id',                         
                        'pop_category_id_conf_multipl',
                        'pop_category_id_country',                        
                        'pop_category_id_country_conf_multipl',
                        'user_doc_ad_sim_categories',                            
                        'user_doc_ad_sim_categories_conf_multipl',
                        'user_doc_ad_sim_topics',                            
                        'user_doc_ad_sim_topics_conf_multipl',
                        'user_doc_ad_sim_entities',                                      
                        'user_doc_ad_sim_entities_conf_multipl',
                        'doc_event_doc_ad_sim_categories',                            
                        'doc_event_doc_ad_sim_categories_conf_multipl',
                        'doc_event_doc_ad_sim_topics',                            
                        'doc_event_doc_ad_sim_topics_conf_multipl',
                        'doc_event_doc_ad_sim_entities',                                 
                        'doc_event_doc_ad_sim_entities_conf_multipl']               

FLOAT_COLUMNS_SIMPLE_BIN_TRANSFORM = [
                                'pop_ad_id_conf',  
                                'pop_document_id_conf',
                                'pop_publisher_id_conf',
                                'pop_advertiser_id_conf',
                                'pop_campain_id_conf',
                                'pop_doc_event_doc_ad_conf',
                                'pop_source_id_conf',
                                'pop_source_id_country_conf',   
                                'pop_entity_id_conf',
                                'pop_entity_id_country_conf',
                                'pop_topic_id_conf',
                                'pop_topic_id_country_conf',
                                'pop_category_id_conf',
                                'pop_category_id_country_conf',
                                'user_doc_ad_sim_categories_conf',
                                'user_doc_ad_sim_topics_conf',
                                'user_doc_ad_sim_entities_conf',
                                'doc_event_doc_ad_sim_categories_conf',
                                'doc_event_doc_ad_sim_topics_conf',
                                'doc_event_doc_ad_sim_entities_conf']
          
FLOAT_COLUMNS = FLOAT_COLUMNS_LOG_BIN_TRANSFORM + FLOAT_COLUMNS_SIMPLE_BIN_TRANSFORM