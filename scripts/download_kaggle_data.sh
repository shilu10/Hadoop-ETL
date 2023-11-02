#/bin/bash
pip3 install kaggle
kaggle datasets download -d olistbr/brazilian-ecommerce
unzip brazilian-ecommerce.zip
mkdir source_data/
cp olist* source_data
