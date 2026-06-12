import type { VisualizationInstruction } from '../services/api'

export function buildA2UILines(item: VisualizationInstruction, surfaceId = 'main'): string[] {
  const instruction = item.a2uiInstruction
  if (!instruction?.componentId) return []

  return [
    JSON.stringify({
      surfaceUpdate: {
        surfaceId,
        components: [
          {
            id: 'root',
            component: {
              [instruction.componentId]: {
                ...(instruction.initialProps ?? {}),
                title: item.title,
                description: item.description,
                componentId: instruction.componentId,
                intentType: instruction.intentType,
                pageId: item.pageId,
                embedUrl: item.embedUrl,
                galleryUrl: item.galleryUrl,
                implementationKind: item.implementationKind,
                fallback: instruction.fallback,
              },
            },
          },
        ],
      },
    }),
    JSON.stringify({
      beginRendering: {
        surfaceId,
        root: 'root',
      },
    }),
  ]
}
