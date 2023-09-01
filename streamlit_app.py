# Import libraries
!pip install pandas --upgrade
import lxml
import pandas as pd
import numpy  as np
import seaborn as sns

import matplotlib.pyplot as plt
import statsmodels.api   as sm
import streamlit         as st


# Import Data Frames
df_bp = pd.read_csv( '/models/business_performance.csv' )
df_bp = df_bp.drop( 'Unnamed: 0', axis=1 )
df_c  = pd.read_csv( '/models/crossprice.csv' )
df_e  = pd.read_csv( '/models/df_elasticity.csv' )


######### Layout Streamlit ############
st.set_page_config( layout='wide' ) 
st.header( 'Price Elasticity of Products' ) 


tab1, tab4, tab5 = st.tabs(( 'Price Ealsticity of Products' , 'Business Performance', ' Cross Price of Products' ))

with tab1:
    tab2, tab3 = st.tabs([ 'Price Elasticity - Graphics', 'Price Elasticity - Data Frame' ])
    with tab2:
        # display price elasticity graphically
        st.header( 'Price Elasticity - Graphics' )
        
        df_e['ranking'] = df_e.loc[:, 'price_elasticity'].rank( ascending=True ).astype(int)
        df_elasticity = df_e.reset_index( drop=True )

        
        fig, ax = plt.subplots() 
        
        plt.figure( figsize=(20, 10) )
        ax.hlines( y=df_elasticity['ranking'], xmin=0, xmax=df_elasticity['price_elasticity'], alpha=1, linewidth=30 )
        
        for name, p in zip( df_elasticity['name'], df_elasticity['ranking'] ):
            ax.text( 4, p, name )
        
            
        # add elasticy labels
        for x, y, s in zip( df_elasticity['price_elasticity'], df_elasticity['ranking'], df_elasticity['price_elasticity']):
            ax.text(x, y, round(s, 2), horizontalalignment='right'if x < 0 else 'left',
                                        verticalalignment='center',
                                        fontdict={'color' : 'red' if x < 0 else 'green', 'size':10 } )
        
        
        #ax.gca().set( ylabel='Ranking Nuber', xlabel = 'Price Elasticity') 
        #ax.title( ' Price Elasticity' )
        ax.grid( linestyle = '--' )
        st.pyplot( fig )

        
    with tab3:
         # display the Cross Price
         st.header( 'Price Elasticity - Data Frame' )
         df_order_elasticity = df_e[[ 'ranking', 'name', 'price_elasticity' ]].sort_values( by='price_elasticity', ascending=False ) 
         st.dataframe( df_order_elasticity )
            
       
with tab4:
    # show Business Performance
    st.header( 'Business Performance' )
    df_bp = df_bp.set_index( 'name' )
    st.dataframe( df_bp, use_container_width = True )

with tab5:
    # Show the Cross Price
    st.header( 'Cross Price Elasticity' )
    df_c = df_c.set_index( 'name' )
    st.dataframe( df_c, use_container_width = True )
