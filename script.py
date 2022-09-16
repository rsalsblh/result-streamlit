import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

images1 = ['pnup.png']
images2 =['indosat.png']
col1, col2, col3 = st.columns([3.5, 1.2, 5])
col2.image(images1, width=70)
col3.image(images2, width=150)

st.title('SISTEM PENDUKUNG KEPUTUSAN STRATEGI PRODUKTIVITAS BASE TRANSCEIVER STATION')

st.markdown("<h3 style='text-align: center;'>Visualisasi Hasil Clustering</h3>", unsafe_allow_html=True)


cluster_df=pd.read_csv("data_cluster.csv")
cluster_df = cluster_df.sort_index()

uploaded_file = st.file_uploader("Pilih Dataset : ")
if uploaded_file is not None :
    dataset = pd.read_csv(uploaded_file)

# JOIN
# join = pca_df.join(cluster_df.cluster, lsuffix='_pca', rsuffix='_cluster')
# join_center = join.join(centers_df, lsuffix='_join1', rsuffix='_center')
# join_center.to_csv('Dataset.csv')

    fig=plt.figure(figsize=[20,10])
    sns.scatterplot(data=dataset, x="PC 1", y="PC 2", hue="cluster", palette="Set2", s = 500, alpha = 0.7)


    # sns.scatterplot(pca_df['PC 1'], pca_df['PC 2'], hue = cluster_df.cluster, palette="Set2", s = 500, alpha = 0.7)

    plt.scatter(dataset['0'], dataset['1'], marker='*', s=300, color='black', label='Centroids')
    plt.legend(prop={'size':18})
    plt.title("Hasil Klustering K-Means",fontsize=20)
    plt.ylabel("PC 2",fontsize=20)
    plt.xlabel("PC 1",fontsize=20)
    st.pyplot(fig)
    # plt.legend()

    st.markdown("<h3 style='text-align: center;'>Pemilihan Strategi Berdasarkan Hasil Clustering</h3>", unsafe_allow_html=True)
    select = st.selectbox('Pilih Strategi',
        ('Akuisisi', 'Penambahan ARPU'))

    if select=='Akuisisi':
        akuisisi = cluster_df['cluster'] == 0
        df_filter_0=cluster_df.loc[akuisisi]
        st.write(df_filter_0)
    else :
        arpu = cluster_df['cluster'] == 1
        df_filter_1=cluster_df.loc[arpu]
        st.write(df_filter_1)






    # import streamlit as st
# import pandas as pd
# import numpy as np
# from PIL import Image
# import plotly.figure_factory as ff

# import matplotlib.pyplot as plt
# # %matplotlib inline
# import seaborn as sns

# images1 = ['pnup.png']
# images2 =['indosat.png']
# col1, col2, col3 = st.columns([3.5, 1.2, 5])
# col2.image(images1, width=70)
# col3.image(images2, width=150)

# st.title('SISTEM PENDUKUNG KEPUTUSAN STRATEGI PRODUKTIVITAS BASE TRANSCEIVER STATION')

# st.markdown("<h3 style='text-align: center;'>Visualisasi Hasil Clustering</h3>", unsafe_allow_html=True)

# PCA_uploaded_files=st.file_uploader("Pilih File PCA")
# if PCA_uploaded_files is not None :
#     pca_df = pd.read_csv(PCA_uploaded_files)
#     st.write(pca_df)
#     # join = pca_df.join(cluster_df.cluster, lsuffix='_pca', rsuffix='_cluster')

# # centers_uploaded_files=st.file_uploader("Pilih File Centers")
# # for centers_uploaded_file in centers_uploaded_files:
# #     centers_df = pd.read_csv(centers_uploaded_file)

# # cluster_uploaded_files=st.file_uploader("Pilih File Cluster")
# # for cluster_uploaded_file in cluster_uploaded_files :
# #     cluster_df = pd.read_csv(cluster_uploaded_file)
# #     cluster_df = cluster_df.sort_index()

# fig=plt.figure(figsize=[20,10])
# sns.scatterplot(data=join, x="PC 1", y="PC 2", hue="cluster", palette="Set2", s = 500, alpha = 0.7)

# plt.scatter(centers_df['0'], centers_df['1'], marker='*', s=300, color='black', label='Centroids')
# plt.legend(prop={'size':18})
# plt.title("Hasil Klustering K-Means",fontsize=20)
# plt.ylabel("PC 2",fontsize=20)
# plt.xlabel("PC 1",fontsize=20)
# st.pyplot(fig)
# # plt.legend()

# st.markdown("<h3 style='text-align: center;'>Pemilihan Strategi Berdasarkan Hasil Clustering</h3>", unsafe_allow_html=True)
# select = st.selectbox('Pilih Strategi',
#     ('Akuisisi', 'Penambahan ARPU'))

# if select=='Akuisisi':
#     akuisisi = cluster_df['cluster'] == 0
#     df_filter_0=cluster_df.loc[akuisisi]
#     st.write(df_filter_0)
# else :
#     arpu = cluster_df['cluster'] == 1
#     df_filter_1=cluster_df.loc[arpu]
#     st.write(df_filter_1)


# # pca_df=pd.read_csv("visualisasi_data_pca.csv")
# # centers_df=pd.read_csv("centers_df.csv")
# # data_cluster=pd.read_csv("data_cluster.csv")

# # cluster_df = cluster_df.sort_index()

# # st.write(pca_df)
# # st.write(cluster_df)


