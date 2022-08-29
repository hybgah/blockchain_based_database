# Blockchain Based Database
This project shows simply how to use a blockchain as a database. Blockchain is a hot topic these days. As a student studying computer science, I think I have to learn about the new trend, at least the basic. The best way to learn about something is to make it from the scratch. A block of a blockchain contains a data. Usually it is an information about the transaction, but every kind of data can be stored. So I came up with an idea to use a blockchain as a database. I have not implemented the decentralization here because I just wanted to understand the strucuture of a blockchain.

## Structure
blockchain.py : Blockchain which can store data.<br>
server.py : Server of the blockchain database.<br>
templates : Html files for the web page.<br>
blockchain_slides.pptx : Slides explaining this project.<br>

## Motivation
Blockchain-based big data is secure and clean. The data in the blockchain can’t be forged. Because adding a block needs always a verification of the whole blocks from multiple users. As the same reason, blockchain can help address problems such as human error, data duplication, and false information often encountered when dealing with huge volumes of data

## How does it work
Program flow is as follows:
<li> User selects how they will input their data. Whether by typing it or uploading a csv file.
<li> They type or upload the data.
<li> If the user upload the data by typing the user have to mine a block, if the data was uploaded by a csv file, the blocks will be mined automatically.
<li> They can show their chain by access the /chain link.

### Blockchain Fundamental
The structure is more complicated, because I’ll focus on the data, which is in the block, I omitted the others. A blockchain consist of lots of blocks. As you can see a block includes data should be stored, two hashes and a timestamp. My chain has just three blocks. But the biggest blockchain is bitcoin and it has more than seven hundred thousand blocks. Then how are the blocks connected and how can we add a block into a blockchain? To understand it we must understand the rule of the hashes.<br>
<img src="https://user-images.githubusercontent.com/62208537/187311744-801bc3b2-6641-4aba-9f0c-be5bb7486d46.png" width="800" height="400"/><br>
The hash of the current block is made by the hash of the previous block and the data of the current block. All the previous hashes effects to the next hashes. So, if a data in a block is changed the hashes of the next blocks will be also changed. Therefore, we can verify through the hashes if the data in the block is manipulated or not. 
<img src="https://user-images.githubusercontent.com/62208537/187312319-3b225071-e4ef-4fe0-a804-7b6e1128a059.png" width="800" height="400"/><br>
