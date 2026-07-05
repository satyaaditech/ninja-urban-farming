import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const klinisTanamanCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/klinis-tanaman' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    category: z.string().default('Klinis Tanaman'),
    tags: z.array(z.string()).default([]),
    type: z.string().default('jamur'),
    symptoms: z.array(z.string()).default([]),
    causes: z.array(z.string()).default([]),
    treatments: z.array(z.string()).default([]),
    prevention: z.string().default(''),
    draft: z.boolean().default(false)
  })
});

const sopCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/sop' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    category: z.string().default('sop'),
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false)
  })
});

const formulasCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/formulas' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    category: z.string().default('formula'),
    tags: z.array(z.string()).default([]),
    ingredients: z.array(z.string()).default([]),
    draft: z.boolean().default(false)
  })
});

const klinisLeleCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/klinis-lele' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    category: z.string().default('Klinis Lele'),
    tags: z.array(z.string()).default([]),
    type: z.string().default('parasit'),
    symptoms: z.array(z.string()).default([]),
    causes: z.array(z.string()).default([]),
    treatments: z.array(z.string()).default([]),
    prevention: z.string().default(''),
    draft: z.boolean().default(false)
  })
});

export const collections = {
  'klinis-tanaman': klinisTanamanCollection,
  'klinis-lele': klinisLeleCollection,
  'sop': sopCollection,
  'formulas': formulasCollection
};
