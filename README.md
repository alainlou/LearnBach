# LearnBach

Hopefully this might make some good music.

[Output examples can be found here](https://github.com/alainlou/LearnBach/tree/master/samples) (download the .mid file and play on Media Player if on Windows or somewhere else on Mac/Unix)

About the Text Data:

Each space is passage of time, more than 1 space means pause of that many time units - 1. There is a 3 second silence between each piece.

About the Repo:

This repo contains a script to download all midi files from a given web page and convert csv files generated from MIDICSV to raw text files and back.

In a sense this is a reverse-engineered version of carykh's processing scripts.

Neural net models were trained with Andrej Karpathy's LSTM using the raw text files and sample output was generated from there.
