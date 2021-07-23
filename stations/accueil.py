################################################################################
### 1. HEADER                                                                ###
################################################################################
# -*- coding: utf-8 -*-

"""
@authors: Phil Scalabrini & Ysael Desage
"""

################################################################################
### 2. IMPORTS                                                               ###
################################################################################

# GENERAL
import streamlit as st
import os


################################################################################
### 3. MAIN CODE                                                             ###
################################################################################

def write(**kwargs):

    #------------------#
    #- SATELLITE VIEW -#
    #------------------#
    st.title("Accueil")
    st.subheader("Outil d’analyse et d'aide à la décision")
    

    st.image(os.path.join("stations","images","accueil.gif"))
    st.header("Utilisation de l'outil")
    st.subheader("Menaces")
    st.markdown("Permet de **_comparer et partager_** rapidement **les impacts des menaces** sur chacune des espèces ciblées par le client.")
    st.subheader("Lac de données")
    st.markdown("Rassembler l'ensemble des **_données disponibles pertinentes_**.")
    st.subheader("Visualisation")
    st.markdown("Visualiser **_la localisation et le nombre d'observation des espèces sur carte_** afin de mieux interpréter leurs intéractions \
         avec l'écosystème de la Rivière des Mille Îles.")
    st.subheader("Analyse")
    st.markdown("Exécute automatiquement des **_analyses statistiques_** en fonction des jeux de données sélectionnés.")
    st.subheader("Intelligence artificielle")
    st.markdown("**Prédiction** et **analyse** par **_intelligence artificielle_** afin de faciliter la prise de décision.")
    #     BC = session_state.BC
    #     BC.synchronize()

    #     # MODULES
    #     st.header('Active modules')
    #     modules_status = list(BC.settings['modules'].values())
    #     modules_name = list(BC.settings['modules'].keys())
    #     modules_status = ['active' if s else 'inactive' for s in modules_status]
    #     modules_version = BC.settings['modules_version']
    #     module_dict = pd.DataFrame({'Status':modules_status   ,
    #                                 'Version':modules_version },
    #                                  index = modules_name     )
    #     st.dataframe(module_dict.style.\
    #            apply(conditional_attribute, op='==', threshold='active', attr='color: green', axis=None).\
    #            apply(conditional_attribute, op='==', threshold='inactive', attr='color: red', axis=None))


    #     # ISSUES
    #     st.header('Issues')
    #     issues_df = access_log(BC.building_id,'issue','',False)
    #     if issues_df.shape[0] > 0: st.write(issues_df.shape[0],'issue(s) reported !')
    #     else: st.write('No issues reported.')
    #     if st.checkbox('Show issues'):
    #         if st.checkbox('raw format'):
    #             issues_df = access_log(BC.building_id,'issue','',True)
    #         cols = list(issues_df.columns)
    #         def_cols = ['severity','error','status','nature','traceback']
    #         selected_cols = st.multiselect("Columns",cols,default=def_cols)
    #         st.dataframe(issues_df[selected_cols])
    #         if issues_df.shape[0] > 0:
    #             if st.button('Clear log'): clear_log(BC.building_id,log='issue')


    #     # ACTIVITY
    #     st.header('Activity Log')
    #     if st.checkbox('Show activity log'):
    #         log_df = access_log(kwargs['BC'].building_id)
    #         cols = list(log_df.columns)
    #         def_cols = ['action','user','status']
    #         selected_cols = st.multiselect("Columns",cols,default=def_cols)
    #         st.dataframe(log_df[selected_cols])


    #     # SATELLITE CONTROLS
    #     st.header('Satellite Controls')
    #     st.subheader('Module Ops')

    #     col11, col12 = st.beta_columns(2)

    #     with col11:
    #         module_selected = st.selectbox('Select module',modules_name)
    #     with col12:
    #         if module_selected is not None:
    #             module_op = st.selectbox('Select action',['None','Terminate','Launch/Update'])
    #             if module_op == 'Launch/Update': version = st.selectbox('Version',['1.0.0'])
    #             if module_op != 'None':
    #                 if st.button(module_op):
    #                     if module_op == 'Launch/Update':
    #                         reset_module(BC.building_id,module_selected)
    #                     elif module_op == 'Terminate': terminate_module(BC.building_id,module_selected)

    #     st.subheader('Process Ops')
    #     processes = load_processes(BC.building_id)
    #     if st.checkbox('Show processes dictionnaries'): st.write(processes)
    #     if processes:
    #         process_names = [v['name'] for v in processes.values()]
    #         process_description = [v['description'] for v in processes.values()]
    #         process_phase = [v['phase'] for v in processes.values()]
    #         process_wave = [v['wave'] for v in processes.values()]
    #         process_period = [v['period'] for v in processes.values()]
    #         process_severity = [v['severity'] for v in processes.values()]
    #         processes_df = pd.DataFrame({'Phase'      :process_phase      ,
    #                                      'Wave'       :process_wave       ,
    #                                      'Period'     :process_period     ,
    #                                      'Severity'   :process_severity   ,
    #                                      'Description':process_description},
    #                                      index = process_names             )

    #         st.dataframe(processes_df)

    #         col21, col22 = st.beta_columns(2)

    #         with col21:
    #             process_selected = st.selectbox('Select process',process_names)
    #             if process_selected is not None: st.write(processes_df['Description'][processes_df.index == process_selected].values[0])
    #         with col22:
    #             if process_selected is not None:
    #                 st.write(' - ')
    #                 if st.button('Remove process'):
    #                     condition = lambda file,process : process['name'] == process_selected
    #                     remove_process_with_condition(BC.building_id,condition)

    #     else: st.write('No currently active processes.')

    #     st.subheader('DANGER ZONE')
    #     if st.button('Terminate Satellite'):
    #         st.write("Please confirm the Satellite's termination order by inputing the Building ID in the box bellow.")
    #         if st.text_input('Confirmation'):
    #             st.write('Terminated !')


    #     # SETTINGS
    #     st.header('Settings')
    #     if st.checkbox('Show instance settings'):
    #         st.json(BC.settings)


    # #------------------------#
    # #- SATELLITE DEPLOYMENT -#
    # #------------------------#
    # else:
    #     if session_state.selected_project is None:
    #         st.error('No project is currently selected.')
    #         st.warning('Select a project to enable satellite deployment')
    #         return

    #     st.title(f"Satellite Deployment")

    #     #- PAGE EMPTY PLACEHOLDERS -#
    #     # Define placeholder
    #     launch_button  = st.empty()     # Launch button
    #     launch_message = st.empty()     # Launched message
    #     img            = st.empty()     # Image/gif

    #     # Configuration files
    #     config_files_section = st.empty()

    #     building_config = st.empty()
    #     building_config_info = st.empty()

    #     system_schedule_up = st.empty()
    #     system_schedule_info = st.empty()

    #     ai_config_up   = st.empty()
    #     ai_config_info = st.empty()
    #     ai_config_butt = st.empty()
    #     full_ai_config = st.empty()

    #     # Settings
    #     settings_section = st.empty()   # Settings section
    #     satellite_file   = st.empty()
    #     settings_info    = st.empty()
    #     settings_box     = st.empty()   # Settings checkbox

    #     #- END OF PLACEHOLDERS -#


    #     # FIRST SECTION - Image and button
    #     launch = launch_button.button('Launch Building Satellite')
    #     img.image(os.path.join(shared_state.projects_path, 'pending_launch.tiff'), use_column_width=True)


    #     # SECOND SECTION - Configuration files
    #     # Building Config
    #     config_files_section.header('Configuration Files')
    #     building_file = building_config.file_uploader('Building Config',['csv'])
    #     if building_file is not None:
    #         building_config_df = pd.read_csv(building_file)
    #         building_config_info.success('Building Config succesfully loaded.')

    #     # System Schedule
    #     config_files_section.header('Configuration Files')
    #     system_schedule = system_schedule_up.file_uploader('System Schedule',['csv'])
    #     if system_schedule is not None:
    #         system_schedule_df = pd.read_csv(system_schedule)
    #         system_schedule_info.success('System schedule succesfully loaded.')

    #     # NOTE [vderm]: Previous:
    #     # # AI Config file
    #     # @st.cache
    #     # def ai_config_validation(ai_config):
    #     #     validation = validate_ai_config(ai_config)
    #     #     return validation

    #     ai_config_file = ai_config_up.file_uploader('AI Config',['json'])
    #     if ai_config_file == None: ai_config_info.info("Leaving this by default will use BuildingKit's generated ai_config.")

    #     if ai_config_file is not None:
    #         ai_config = load_json_file(ai_config_file)

    #         # NOTE [vderm]: New:
    #         ai_config_file_test_success = st_validate_ai_config(ai_config)
    #         # NOTE [vderm]: Previous:
    #             # with st.spinner('Validating AI Config ...'):
    #             #     ai_config = load_json_file(ai_config_file)
    #             #     try:
    #             #         validation = ai_config_validation(ai_config)
    #             #         ai_config_info.success('AI Config successfuly loaded and validated !')
    #             #         if ai_config_butt.checkbox('View config'):
    #             #             full_ai_config.json(ai_config)

    #             #         # Save ai_config in corresponding directory
    #             #         #with open('home/ysael/Projects/Livmore/ai_config.json', 'w') as outfile:
    #             #         # with open('ai_config.json', 'w') as outfile:
    #             #         #     json.dump(ai_config, outfile)

    #             #     except:
    #             #         ai_config_info.error('Rejected AI Config, please verify structure.'+traceback.format_exc())


    #     # THIRD SECTION - Settings
    #     settings_section.header('Settings')
    #     settings = settings_box.checkbox('Modify default launch settings')

    #     with open('build_sat_ref.json','r') as f:
    #             config = json.load(f)
    #             config['building_id'] = session_state.bldg_info['bldg_id'].item()

    #     if settings:

    #         st.subheader('Satellite Config')

    #         config_in = satellite_file.file_uploader('Satellite Config')
    #         settings_info.info('To modify settings, copy the file bellow using the blue symbol next to the first dictionnary bracket, apply your modifications in a new JSON file, then submit it back above.')

    #         if config_in != None: config = load_json_file(config_in)
    #         out = st.json(config)

    #     # TODO: Finalize actual launch, code deploys for bldg_id = 61 in Ysael's desktop
    #     if launch:

    #         if building_config == None or system_schedule == None:
    #             launch_message.error('Missing file(s). Please input at least building config and system schedule.')
    #         else:
    #             launch_message.info("Launching Satellite! [PLACEHOLDER]")
    #             launch_button.empty()

    #             #- PAGE EMPTY PLACEHOLDERS -#
    #             # Define placeholder
    #             launch_button.empty()     # Launch button
    #             launch_message.empty()     # Launched message
    #             config_files_section.empty()

    #             building_config.empty()
    #             building_config_info.empty()

    #             system_schedule_up.empty()
    #             system_schedule_info.empty()

    #             ai_config_up.empty()
    #             ai_config_info.empty()
    #             ai_config_butt.empty()
    #             full_ai_config.empty()

    #             settings_section.empty()
    #             satellite_file.empty()
    #             settings_info.empty()
    #             settings_box.empty()

    #             img.image(os.path.join(shared_state.projects_path,'launch.gif'), use_column_width=True)

    #             os.system('python main.py -b 61')
    #             time.sleep(16)
    #             img.empty()

    #             #directory = '/home/brainbox/projects'
    #             directory = '/Users/ysaeldesage/Desktop'

    #             # Get final directory
    #             building_info = retrieve_building_info_from_db(session_state.bldg_info['bldg_id'].item())

    #             # Define instance name as building name
    #             final_dir = str(session_state.bldg_info['bldg_id'].item())+'_'+building_info['building_name']
    #             bk_directory = os.path.join(directory,final_dir,'Building_Kit')
    #             full_directory = os.path.join(directory,final_dir)

    #             building_config_df.to_csv(os.path.join(bk_directory,'building_config.csv'))
    #             system_schedule_df.to_csv(os.path.join(bk_directory,'System_Schedule.csv'))

    #             if ai_config_file is not None:
    #                 if ai_config_file_test_success:
    #                     with open(os.path.join(full_directory,'ai_config.json'),'w') as f:
    #                         json.dump(ai_config, f,indent=4)
    #                 else:
    #                     # TODO: Ysael, what should you do if the ai_config is bad?
    #                     pass

    #             with open(os.path.join(full_directory,'satellite_config.json'),'w') as f:
    #                json.dump(config, f,indent=4)

    #             st.success('Launch successful !')
    #             #st.write("<p> Launch <span style='color:green'> successful </span> </p>",
    #             #            unsafe_allow_html=True)

################################################################################
### X. ENF OF CODE                                                           ###
################################################################################