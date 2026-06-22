interface MdastNode {
  type: string;
  lang?: string;
  value?: string;
  children?: MdastNode[];
  [key: string]: unknown;
}

export default function remarkMermaid() {
  return (tree: MdastNode) => {
    if (!tree.children) return;
    for (let i = 0; i < tree.children.length; i++) {
      const node = tree.children[i];
      if (node.type === 'code' && node.lang === 'mermaid') {
        tree.children[i] = {
          type: 'mdxJsxFlowElement',
          name: 'Mermaid',
          attributes: [
            {
              type: 'mdxJsxAttribute',
              name: 'chart',
              value: node.value ?? '',
            },
          ],
          children: [],
        };
      }
    }
  };
}
