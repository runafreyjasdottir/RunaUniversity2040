# CS207: Introduction to Machine Learning
## Bachelor of Science in Computer Science — University of Yggdrasil, 2040

**Credits:** 4  
**Prerequisites:** CS102 — Discrete Mathematics for CS; CS104 — Object-Oriented Programming; CS201 — Data Structures & Algorithms II  
**Description:** Supervised and unsupervised learning, neural networks, backpropagation, SVMs, ensemble methods, deep learning foundations. Practical exercises in PyTorch and JAX on the Yggdrasil Mimir Research Cluster.

---

## Lecture 1: The Learning Problem — What Does It Mean to Learn?

Machine learning is the study of algorithms that improve their performance on a task as they are given more data. Tom Mitchell's 1997 formulation provides the canonical definition: a computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E. This definition is deliberately broad — it encompasses everything from linear regression (which improves its prediction of housing prices as it sees more houses) to modern foundation models (which improve their text generation as they process more tokens from the internet). The unifying insight is that learning is generalisation from experience — the capacity to perform well on data that the learner has not seen before, by extracting patterns from data that it has.

The formal setup frames every machine learning problem as a search through a hypothesis space. We have an input domain X (the set of possible inputs), a label space Y (the set of possible outputs), and an unknown target function f: X → Y that we wish to approximate. We receive a training set D = {(x₁, y₁), ..., (xₙ, yₙ)} drawn from an unknown distribution P over X × Y, and we seek a hypothesis h: X → Y (drawn from hypothesis class H) that minimises the expected loss R(h) = E_{(x,y)~P}[L(h,(x,y))]. Since P is unknown, we can only compute the empirical risk R̂(h) = (1/n)Σᵢ L(h,(xᵢ,yᵢ)). The empirical risk minimisation principle selects h minimising R̂(h), but this permits overfitting: a hypothesis achieving zero training error may generalise poorly because it memorises noise rather than learning structure. Regularisation — adding penalties for complexity or restricting H — is the countermeasure.

**Bias-variance decomposition** illuminates the fundamental tradeoff. For regression with squared loss, expected prediction error decomposes into bias² (systematic error from the algorithm's inductive preferences), variance (sensitivity to the particular training sample), and irreducible error (noise no algorithm can eliminate). High bias means underfitting; high variance means overfitting. The sweet spot balances expressiveness against stability — this tension is invariant to the algorithm, a property of the learning problem itself.

**PAC learning** (Probably Approximately Correct) provides the theoretical scaffolding. A concept class C is PAC-learnable if there exists an algorithm that, for any ε > 0 and δ > 0 and for any distribution P over X, outputs a hypothesis h with error at most ε with probability at least 1−δ, given poly(1/ε,1/δ,n) examples. The **VC dimension** measures hypothesis class expressiveness: the largest number of points H can shatter. Sample complexity scales as O((d_VC/ε)log(1/ε) + log(1/δ)). **No free lunch theorems** (Wolpert, 1996) establish that no algorithm dominates on average over all distributions — every hypothesis class encodes an inductive bias, a bet on the world's structure.

The **supervised/unsupervised/reinforcement** taxonomy partitions learning by feedback type. Each paradigm has distinct assumptions, algorithms, and guarantees — covered in subsequent lectures.

**Required Reading:**
- Tom Mitchell, *Machine Learning* (McGraw-Hill, 1997/2040), chs. 1–2
- Shai Shalev-Shwartz & Shai Ben-David, *Understanding Machine Learning* (Cambridge UP, 2014/2040), chs. 1–3
- Yggdrasil ML Lab: Bias-Variance Decomposition, VC Dimension Explorer (2040)

**Discussion Questions:**
1. Does deep learning violate the bias-variance tradeoff, or does it shift the sweet spot when datasets become very large?
2. The no free lunch theorems render no algorithm universally superior. Does this make algorithm selection meaningless, or does it elevate it to a meta-learning problem?
3. PAC learnability guarantees have sample complexity bounds that far exceed practical needs. What explains the gap between theory and practice?

---

## Lecture 2: Linear Models — Regression and Classification

Linear regression finds weights w ∈ ℝᵈ and bias b minimising MSE: L(w,b) = (1/n)Σᵢ(wᵀxᵢ+b−yᵢ)². The OLS solution w* = (XᵀX)⁻¹Xᵀy is BLUE under Gauss-Markov assumptions. When assumptions fail — nonlinearity, heteroscedasticity, correlated errors — remedies include transformations, weighted least squares, and generalised least squares.

Regularisation prevents overfitting. **Ridge** (L₂) adds λ||w||², shrinking weights toward zero and ensuring invertibility of XᵀX+λI. **Lasso** (L₁) adds λ||w||₁, producing sparse solutions for automatic feature selection. **Elastic Net** blends both. **Logistic regression** models P(y=1|x) = σ(wᵀx+b) with binary cross-entropy loss, producing a linear decision boundary. **Multiclass logistic regression** uses softmax and categorical cross-entropy.

**Gradient descent** updates w ← w − η∇L(w). **SGD** approximates gradients using mini-batches. **Adam** (Kingma & Ba, 2015) combines adaptive learning rates with momentum, serving as the default optimiser for deep learning in PyTorch and JAX.

**Required Reading:**
- Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning* (2nd ed., 2009/2040), chs. 3–4
- Bishop, *Pattern Recognition and Machine Learning* (2006/2040), chs. 3–4
- Yggdrasil ML Lab: Linear Regression, Logistic Regression, Regularisation (2040)

**Discussion Questions:**
1. What are the most common violations of linear regression assumptions, and how can you detect and address them?
2. Under what conditions does Lasso fail to select the correct features?
3. What practical strategies help avoid poor local minima in non-convex optimisation?

---

## Lecture 3: Decision Trees and Ensemble Methods — The Wisdom of Crowds

Decision trees partition input space with axis-aligned splits. Splitting criteria include Gini impurity and entropy for classification, variance reduction for regression. Overfitting is addressed by pre-pruning (stopping early) and post-pruning (cost-complexity pruning with parameter α).

**Random forests** (Breiman, 2001) combine many trees via bagging with bootstrap sampling and random feature subsetting. Out-of-bag error provides efficient cross-validation. **Gradient boosting** (Friedman, 2001) builds trees sequentially, each fitting the negative gradient. **XGBoost** (Chen & Guestrin, 2016) adds regularisation, sparse-aware splitting, and cache-aware access. **LightGBM** uses histogram-based splitting for speed. **CatBoost** handles categorical features via ordered target statistics. Gradient boosting typically wins on tabular data; random forests are faster, more robust, and more interpretable.

SHAP values (Lundberg & Lee, 2017) provide local explanations by fairly allocating predictions among features using Shapley values from cooperative game theory, guaranteeing local accuracy and consistency.

**Required Reading:**
- Breiman, "Random Forests," *Machine Learning* 45:1 (2001): 5–32
- Friedman, "Greedy Function Approximation: A Gradient Boosting Machine," *Annals of Statistics* 29:5 (2001)
- Chen & Guestrin, "XGBoost," *KDD '16* (2016): 785–794
- Lundberg & Lee, "A Unified Approach to Interpreting Model Predictions," *NeurIPS '17* (2017)

**Discussion Questions:**
1. Is there a fundamental interpretability-accuracy tradeoff, or can we have both?
2. XGBoost dominates tabular data while neural networks dominate unstructured data. Why this divide?
3. Are SHAP values genuine explanations or merely decompositions?

---

## Lecture 4: Support Vector Machines and Kernel Methods

SVMs find the maximum-margin hyperplane minimising ||w||²/2 subject to yᵢ(wᵀxᵢ+b) ≥ 1. The solution depends only on **support vectors** — training points on the margin boundary. The soft-margin SVM introduces slack variables ξᵢ and regularisation parameter C. The dual formulation depends on data only through inner products, enabling the **kernel trick**: replacing ⟨xᵢ,xⱼ⟩ with K(xᵢ,xⱼ) = ⟨φ(xᵢ),φ(xⱼ)⟩ implicitly maps to high-dimensional feature spaces.

Standard kernels: Linear, Polynomial, RBF (universal kernel mapping to ∞ dimensions), Sigmoid. **Mercer's theorem** guarantees that any PSD kernel corresponds to an inner product in some feature space. The kernel trick extends beyond SVMs to kernel PCA, kernel k-means, and kernel ridge regression. Computational limitations (O(n²) storage, O(n³) time for the Gram matrix) are addressed by Random Fourier Features and Nyström approximation.

**Required Reading:**
- Bishop, *Pattern Recognition and Machine Learning* (2006/2040), chs. 6–7
- Schölkopf & Smola, *Learning with Kernels* (MIT Press, 2002/2040)
- Cortes & Vapnik, "Support-Vector Networks," *Machine Learning* 20:3 (1995): 273–297

**Discussion Questions:**
1. What is the relationship between the soft-margin SVM and logistic regression in the limit of small C?
2. The RBF kernel maps to infinite dimensions. Why doesn't this overfit, and what role does the margin play?
3. When are approximate kernel methods justified?

---

## Lecture 5: Neural Networks and Backpropagation

Artificial neurons compute a = σ(wᵀx+b). Activations: sigmoid, tanh, ReLU (modern default), Leaky ReLU, ELU, GELU, Swish. Feedforward networks compose layers: ŷ = σ_L(W_L ...σ₁(W₁x+b₁)...+b_L). The universal approximation theorem (Cybenko 1989) guarantees expressiveness with sufficient width, but depth provides **efficiency**: deep networks represent certain functions with exponentially fewer neurons than shallow ones.

Backpropagation (Rumelhart, Hinton & Williams, 1986) computes gradients via the chain rule in reverse order. Cost is 2–3× the forward pass. The vanishing gradient problem (Hochreiter 1991) plagues early layers; solutions include ReLU, batch normalisation, and residual connections. Weight initialisation: Xavier/Glorot (Var = 2/(nₗ+nₗ₊₁)) for sigmoid/tanh, He (Var = 2/nₗ) for ReLU.

**Required Reading:**
- Goodfellow, Bengio & Courville, *Deep Learning* (2016/2040), chs. 6–8
- Rumelhart, Hinton & Williams, "Learning Representations by Back-Propagating Errors," *Nature* 323 (1986): 533–536
- Glorot & Bengio, "Understanding the Difficulty of Training Deep Feedforward Neural Networks," *AISTATS '10* (2010)

**Discussion Questions:**
1. Why are deep networks more effective than wide shallow ones?
2. Compare how ReLU, batch normalisation, and residual connections address vanishing gradients.
3. What are the hardware implications of backpropagation for billion-parameter networks?

---

## Lecture 6: Convolutional Neural Networks — Vision and the Architecture of Perception

CNNs exploit grid-like data through local connectivity, weight sharing, and translation equivariance. Architectural evolution: LeNet-5 (1998, ~60K params) → AlexNet (2012, 60M params, ReLU, dropout, GPU) → VGGNet (2014, 16–19 layers) → GoogLeNet/Inception (2015, multi-scale filters) → ResNet (2016, residual connections, 152 layers, better-than-human ImageNet performance).

Transfer learning uses pre-trained models (ImageNet) as starting points. Fine-tuning achieves strong performance with few labels. Data augmentation (flipping, cropping, MixUp, CutMix, RandAugment) expands training distributions. In 2040, the Yggdrasil CV Library provides pre-trained ResNet-50, EfficientNet-V2, and ViT-B/16.

**Required Reading:**
- Goodfellow, Bengio & Courville, *Deep Learning* (2016/2040), ch. 9
- He et al., "Deep Residual Learning for Image Recognition," *CVPR '16* (2016)
- LeCun, Bengio & Hinton, "Deep Learning," *Nature* 521 (2015): 436–444

**Discussion Questions:**
1. What assumptions does CNN weight sharing encode, and when do they fail?
2. Do residual connections change representable functions, or just make optimisation easier?
3. What are ethical implications of ImageNet pre-training for non-Western contexts?

---

## Lecture 7: Recurrent Neural Networks and Sequence Modelling

RNNs process sequential data via hidden state hₜ = f(Wₕₕh_{t−1}+Wₓₕxₜ+bₕ). Vanilla RNNs suffer from vanishing gradients, limiting effective memory to ~10–20 time steps. **LSTM** (Hochreiter & Schmidhuber, 1997) introduces forget, input, and output gates plus a cell state cₜ = fₜ⊙c_{t−1}+iₜ⊙c̃ₜ providing unobstructed gradient flow. **GRU** (Cho et al., 2014) simplifies with ~25% fewer parameters.

Bidirectional RNNs process both directions: hₜ = [→hₜ;←hₜ]. Sequence-to-sequence models (Sutskever et al., 2014) encode input and decode output; **attention** (Bahdanau et al., 2015) eliminates the information bottleneck. **Transformers** (Vaswani et al., 2017) replace recurrence with self-attention: Attention(Q,K,V) = softmax(QKᵀ/√dₖ)V. Multi-head attention, position-wise feed-forward networks, layer normalisation, and positional encodings. The architecture underpins BERT, GPT, T5, and every major language model in 2040.

**Required Reading:**
- Hochreiter & Schmidhuber, "Long Short-Term Memory," *Neural Computation* 9:8 (1997): 1735–1780
- Bahdanau, Cho & Bengio, "Neural Machine Translation by Jointly Learning to Align and Translate," *ICLR '15* (2015)
- Vaswani et al., "Attention Is All You Need," *NeurIPS '17* (2017): 5998–6008

**Discussion Questions:**
1. LSTMs still struggle with sequences >1000 time steps. Why?
2. Self-attention is O(n²) while RNNs are O(n). Why have Transformers replaced RNNs?
3. How does neural attention relate to human cognitive attention?

---

## Lecture 8: Unsupervised Learning — Clustering, Dimensionality Reduction, and Generative Models

Unsupervised learning discovers structure in unlabelled data. **K-means** partitions n points into k clusters minimising within-cluster sum of squares, alternating between assignment and centroid update. It converges to local minima, is sensitive to initialisation (addressed by K-means++), and requires k a priori. **Hierarchical clustering** builds dendrograms via agglomerative or divisive strategies with various linkage criteria (single, complete, average, Ward's), but costs O(n²) time and space.

**PCA** finds orthogonal directions of maximum variance via eigendecomposition of XXᵀ or SVD of centred X. It is optimal for reconstruction error minimisation. **Autoencoders** learn compressed representations through an encoder-decoder architecture trained to reconstruct input. **Variational autoencoders** (Kingma & Welling, 2014) add probabilistic interpretation: the encoder outputs Gaussian parameters, training maximises the ELBO = E[log p(x|z)] − KL(q(z|x)||p(z)), and the prior enables generation by sampling z ~ N(0,I) and decoding.

**GANs** (Goodfellow et al., 2014) pit a generator G against a discriminator D in a minimax game. Failure modes include mode collapse, training instability, and vanishing gradients. **Diffusion models** (Ho et al., 2020) define a forward process that adds Gaussian noise over T steps and a reverse process that learns to denoise. They are more stable than GANs, produce higher-quality samples than VAEs, and are the foundation of state-of-the-art image/video generation in 2040.

**Required Reading:**
- Goodfellow et al., "Generative Adversarial Nets," *NeurIPS '14* (2014): 2672–2680
- Kingma & Welling, "Auto-Encoding Variational Bayes," *ICLR '14* (2014)
- Ho, Jain & Abbeel, "Denoising Diffusion Probabilistic Models," *NeurIPS '20* (2020): 6840–6851
- Bishop, *Pattern Recognition and Machine Learning* (2006/2040), chs. 9, 12

**Discussion Questions:**
1. What are the limitations of k-means++ for choosing k, and what alternatives exist?
2. What are GAN failure modes and how have subsequent architectures addressed them?
3. Why have diffusion models replaced GANs for image generation, and what are their disadvantages?

---

## Lecture 9: Reinforcement Learning — Learning from Rewards

Reinforcement learning studies agents that learn from scalar rewards, balancing exploration and exploitation. The **MDP** framework: (S, A, P, R, γ) defines states, actions, transition probabilities, rewards, and discount factor. The agent seeks a policy π maximising the expected discounted return V^π(s) = E[Σₜ γᵗRₜ|s₀=s]. The **value function** V^π and **action-value function** Q^π satisfy Bellman equations. The optimal value function V* maximises over all policies.

**Q-learning** (Watkins, 1989) is an off-policy TD algorithm: Q(s,a) ← Q(s,a) + α[R + γmax_a'Q(s',a') − Q(s,a)]. **DQN** (Mnih et al., 2015) extends Q-learning to high-dimensional states via neural networks, stabilised by experience replay and target networks. DQN achieved human-level performance on 29/49 Atari games.

**Policy gradient methods** learn π_θ directly. The policy gradient theorem (Sutton et al., 2000): ∇θJ(θ) = E[∇θlogπ_θ(a|s)·Q^π(s,a)]. **REINFORCE** (Williams, 1992) is the simplest algorithm. Variance is reduced by baselines, advantage functions, and actor-critic methods. **PPO** (Schulman et al., 2017) constrains policy updates via clipping, preventing destructively large updates. PPO is the default for RLHF training of large language models in 2040.

**Required Reading:**
- Sutton & Barto, *Reinforcement Learning: An Introduction* (2nd ed., 2018/2040), chs. 3–6, 8–9, 13
- Mnih et al., "Human-Level Control Through Deep Reinforcement Learning," *Nature* 518 (2015): 529–533
- Schulman et al., "Proximal Policy Optim