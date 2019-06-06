# COS960
COS960 is a Chinese word similarity dataset of 960 word pairs. Each pair of words is annotated by  15 native speakers with a similarity score which reflects **true similarity**. The 960 word pairs are further divided into 3 groups according to their Part Of Speech tags, including 480 pairs of nouns, 240 pairs of verbs and 240 pairs of adjectives.

### Usage

To use COS960 to test your word embedding, use command

```
python correlation_calcu.py {VECTOR_FILE}
```

### Dataset

The data in the files is formulated as

```
[Word1] [Word2] [Average] [Annotator1] ... [Annotator15]

小心谨慎  谨慎小心     4.0         4      ...       4 
```

### Cite

If you  use the dataset, please cite this:

```
@article{huang2019COS960,
Author = {Junjie Huang and Fanchao Qi and Chenghao Yang and Zhiyuan Liu and Maosong Sun},
Title = {{COS960: A Chinese Word Similarity Dataset of 960 Word Pairs}},
journal={arXiv preprint arXiv:1906.00247},
Year = {2019},
}
```

