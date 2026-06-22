import Link from 'next/link';
import {
  BookOpen,
  Code2,
  Layers,
  Users,
  ArrowRight,
  GraduationCap,
  Cpu,
  Sparkles,
  Brain,
} from 'lucide-react';

const features = [
  {
    icon: BookOpen,
    title: '零基础友好',
    desc: '不需要预先掌握复杂的数学知识，用到什么讲什么。',
  },
  {
    icon: Code2,
    title: '代码驱动',
    desc: '每个知识点都配有可运行的代码示例，边学边练。',
  },
  {
    icon: Layers,
    title: '由浅入深',
    desc: '从线性回归到深度神经网络，循序渐进稳步提升。',
  },
  {
    icon: Users,
    title: '社区精选',
    desc: '融合南瓜书、蘑菇书、苹果书等 Datawhale 经典教程精华。',
  },
];

const foundations = [
  '机器学习概述',
  '线性代数基础',
  '概率与统计',
  'Python 与 NumPy',
  '数据预处理',
  '线性回归',
  '逻辑回归',
  '梯度下降',
  '模型评估',
  '过拟合与正则化',
];

const deepLearning = [
  '神经网络基础',
  '反向传播算法',
  '激活函数',
  '卷积神经网络 CNN',
  '循环神经网络 RNN/LSTM',
  '优化算法',
  '批归一化与 Dropout',
  'PyTorch 基础',
  '训练技巧',
  '迁移学习',
];

const generativeAi = [
  '生成模型概述',
  '变分自编码器 VAE',
  '生成对抗网络 GAN',
  '扩散模型',
];

const llm = [
  'NLP 基础',
  '词嵌入与 Transformer',
  '注意力机制',
  '预训练语言模型',
  'GPT 系列',
  'BERT 与微调',
  '提示工程',
  'RAG 检索增强生成',
  '大模型部署',
  'AI Agent',
  '多模态大模型',
  '大模型评估',
  'RLHF 与对齐',
  '安全与伦理',
  '前沿进展',
  '项目实战',
];

export default function HomePage() {
  return (
    <main className="flex flex-col">
      {/* Hero */}
      <section className="relative overflow-hidden hero-gradient text-white">
        <div className="hero-glow w-[500px] h-[500px] bg-cyan-300 top-[-100px] left-[-100px]" />
        <div className="hero-glow w-[400px] h-[400px] bg-teal-200 bottom-[-80px] right-[-60px]" />
        <div className="relative z-10 flex flex-col items-center justify-center min-h-[520px] px-6 text-center">
          <div className="animate-fade-in-up flex items-center gap-2 mb-6 rounded-full bg-white/15 px-4 py-1.5 text-sm font-medium backdrop-blur-sm">
            <Sparkles className="w-4 h-4" />
            从零到一，系统掌握 AI
          </div>
          <h1 className="animate-fade-in-up text-5xl sm:text-6xl font-extrabold tracking-tight mb-4">
            HAPPY-AI
          </h1>
          <p className="animate-fade-in-up-delay-1 text-xl sm:text-2xl font-medium text-white/90 mb-2">
            机器学习与深度学习教程
          </p>
          <p className="animate-fade-in-up-delay-2 text-base sm:text-lg text-white/75 max-w-xl mb-10">
            由浅入深的系统性 AI 学习路线，涵盖数学基础、经典算法、神经网络与 PyTorch 实战。
          </p>
          <div className="animate-fade-in-up-delay-2 flex flex-col sm:flex-row gap-4">
            <Link
              href="/docs"
              className="inline-flex items-center gap-2 rounded-full bg-white px-7 py-3 text-base font-semibold text-teal-700 shadow-lg hover:bg-white/90 transition-colors"
            >
              开始学习
              <ArrowRight className="w-4 h-4" />
            </Link>
            <Link
              href="/docs/foundations/01-intro-ml"
              className="inline-flex items-center gap-2 rounded-full border border-white/40 px-7 py-3 text-base font-semibold text-white hover:bg-white/15 transition-colors"
            >
              基础篇
            </Link>
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-20 px-6">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-4 text-fd-foreground">
            教程特色
          </h2>
          <p className="text-center text-fd-muted-foreground mb-12 max-w-lg mx-auto">
            精心设计的学习体验，让 AI 学习不再困难
          </p>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
            {features.map((f) => (
              <div
                key={f.title}
                className="feature-card card-glass rounded-2xl p-6 flex flex-col items-center text-center"
              >
                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-teal-400 to-cyan-500 flex items-center justify-center mb-4 shadow-md">
                  <f.icon className="w-6 h-6 text-white" />
                </div>
                <h3 className="text-lg font-semibold mb-2 text-fd-foreground">
                  {f.title}
                </h3>
                <p className="text-sm text-fd-muted-foreground leading-relaxed">
                  {f.desc}
                </p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Course Overview */}
      <section className="py-20 px-6 bg-fd-muted/50">
        <div className="max-w-5xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-4 text-fd-foreground">
            课程目录
          </h2>
          <p className="text-center text-fd-muted-foreground mb-12 max-w-lg mx-auto">
            40 个章节，从入门到实战的完整学习路径
          </p>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <CourseCard
              icon={GraduationCap}
              title="基础篇"
              subtitle="机器学习入门"
              chapters={foundations}
              href="/docs/foundations/01-intro-ml"
              color="from-teal-500 to-emerald-500"
            />
            <CourseCard
              icon={Cpu}
              title="深度学习篇"
              subtitle="深度学习"
              chapters={deepLearning}
              href="/docs/deep-learning/11-neural-networks"
              color="from-cyan-500 to-blue-500"
            />
            <CourseCard
              icon={Sparkles}
              title="生成式 AI 篇"
              subtitle="生成式人工智能"
              chapters={generativeAi}
              href="/docs/generative-ai/21-generative-models"
              color="from-purple-500 to-pink-500"
            />
            <CourseCard
              icon={Brain}
              title="LLM 篇"
              subtitle="大语言模型"
              chapters={llm}
              href="/docs/llm/25-nlp-foundations"
              color="from-orange-500 to-red-500"
            />
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-10 px-6 border-t border-fd-border">
        <div className="max-w-5xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4 text-sm text-fd-muted-foreground">
          <span>HAPPY-AI &copy; {new Date().getFullYear()}</span>
          <div className="flex items-center gap-4">
            <Link href="/docs" className="hover:text-fd-primary transition-colors">
              文档
            </Link>
            <a
              href="https://github.com/fuma-nama/fumadocs"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:text-fd-primary transition-colors"
            >
              GitHub
            </a>
          </div>
        </div>
      </footer>
    </main>
  );
}

function CourseCard({
  icon: Icon,
  title,
  subtitle,
  chapters,
  href,
  color,
}: {
  icon: React.ComponentType<{ className?: string }>;
  title: string;
  subtitle: string;
  chapters: string[];
  href: string;
  color: string;
}) {
  return (
    <div className="card-glass rounded-2xl p-6 flex flex-col">
      <div className="flex items-center gap-3 mb-4">
        <div
          className={`w-10 h-10 rounded-lg bg-gradient-to-br ${color} flex items-center justify-center shadow-md`}
        >
          <Icon className="w-5 h-5 text-white" />
        </div>
        <div>
          <h3 className="text-lg font-semibold text-fd-foreground">{title}</h3>
          <p className="text-xs text-fd-muted-foreground">{subtitle}</p>
        </div>
      </div>
      <ul className="space-y-1.5 mb-6 flex-1">
        {chapters.map((ch, i) => (
          <li key={ch} className="flex items-start gap-2 text-sm text-fd-muted-foreground">
            <span className="shrink-0 w-5 text-right text-xs font-mono text-fd-primary/70">
              {String(i + 1).padStart(2, '0')}
            </span>
            {ch}
          </li>
        ))}
      </ul>
      <Link
        href={href}
        className="inline-flex items-center gap-1.5 text-sm font-medium text-fd-primary hover:underline"
      >
        开始学习
        <ArrowRight className="w-3.5 h-3.5" />
      </Link>
    </div>
  );
}
