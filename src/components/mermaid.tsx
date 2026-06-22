'use client';

import { useEffect, useId, useRef, useState } from 'react';
import mermaid from 'mermaid';

let initialized = false;

function initMermaid() {
  if (initialized) return;
  mermaid.initialize({
    startOnLoad: false,
    theme: 'default',
    themeVariables: {
      primaryColor: '#0d9488',
      primaryTextColor: '#fff',
      primaryBorderColor: '#0d9488',
      lineColor: '#06b6d4',
      secondaryColor: '#ccfbf1',
      tertiaryColor: '#f0fdfa',
    },
  });
  initialized = true;
}

export function Mermaid({ chart }: { chart: string }) {
  const id = useId().replace(/:/g, 'm');
  const ref = useRef<HTMLDivElement>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    initMermaid();
    let cancelled = false;

    async function render() {
      try {
        const { svg } = await mermaid.render(`mermaid-${id}`, chart);
        if (!cancelled && ref.current) {
          ref.current.innerHTML = svg;
          setError(null);
        }
      } catch (e) {
        if (!cancelled) {
          setError(e instanceof Error ? e.message : 'Mermaid render error');
        }
      }
    }

    render();
    return () => {
      cancelled = true;
    };
  }, [chart, id]);

  if (error) {
    return (
      <pre className="rounded-lg bg-red-50 p-4 text-sm text-red-600 dark:bg-red-950/30 dark:text-red-400">
        {error}
      </pre>
    );
  }

  return (
    <div
      ref={ref}
      className="my-6 flex justify-center overflow-x-auto [&>svg]:max-w-full"
    />
  );
}
