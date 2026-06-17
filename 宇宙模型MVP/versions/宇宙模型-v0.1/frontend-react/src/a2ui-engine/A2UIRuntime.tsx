import type { ComponentType, ReactNode } from 'react'
import { EclipseGeometry, EclipticLunarPath, EphemerisComparison, GeocentricDailyMotion } from '../astronomy-components'
import { GenericVisualization } from './GenericVisualization'

type A2UIComponentNode = {
  id: string
  component: Record<string, Record<string, unknown>>
}

type SurfaceState = {
  components: Record<string, A2UIComponentNode>
  data: Record<string, unknown>
  root: string | null
}

type RegistryComponentProps = {
  node: Record<string, unknown>
  data: Record<string, unknown>
}

const registry = new Map<string, ComponentType<RegistryComponentProps>>()

registry.set('astronomy-core.ecliptic-lunar-path', EclipticLunarPath)
registry.set('astronomy-core.eclipse-geometry', EclipseGeometry)
registry.set('astronomy-core.ephemeris-comparison', EphemerisComparison)
registry.set('astronomy-core.geocentric-daily-motion', GeocentricDailyMotion)

function getComponentType(node: A2UIComponentNode): [string, Record<string, unknown>] | null {
  const [name, props] = Object.entries(node.component)[0] ?? []
  if (!name || !props) return null
  return [name, props]
}

export function applyA2UILine(surface: SurfaceState, line: string): SurfaceState {
  const message = JSON.parse(line) as Record<string, unknown>
  const next: SurfaceState = {
    components: { ...surface.components },
    data: { ...surface.data },
    root: surface.root,
  }

  const surfaceUpdate = message.surfaceUpdate as { components?: A2UIComponentNode[] } | undefined
  if (surfaceUpdate?.components) {
    for (const component of surfaceUpdate.components) {
      next.components[component.id] = component
    }
  }

  const dataModelUpdate = message.dataModelUpdate as
    | { contents?: Array<{ key: string; valueString?: string; valueNumber?: number; valueBoolean?: boolean }> }
    | undefined
  if (dataModelUpdate?.contents) {
    for (const item of dataModelUpdate.contents) {
      if ('valueString' in item) next.data[item.key] = item.valueString
      if ('valueNumber' in item) next.data[item.key] = item.valueNumber
      if ('valueBoolean' in item) next.data[item.key] = item.valueBoolean
    }
  }

  const beginRendering = message.beginRendering as { root?: string } | undefined
  if (beginRendering?.root) {
    next.root = beginRendering.root
  }

  const deleteSurface = message.deleteSurface
  if (deleteSurface) {
    return createEmptySurface()
  }

  return next
}

export function createEmptySurface(): SurfaceState {
  return { components: {}, data: {}, root: null }
}

function renderBuiltIn(
  type: string,
  props: Record<string, unknown>,
  surface: SurfaceState,
  renderById: (id: string) => ReactNode,
): ReactNode {
  if (type === 'Text') {
    const text = props.text as { literalString?: string } | undefined
    return <p className="a2ui-text">{text?.literalString ?? ''}</p>
  }

  if (type === 'Column') {
    const children = props.children as { explicitList?: string[] } | undefined
    return <div className="a2ui-column">{children?.explicitList?.map(renderById)}</div>
  }

  if (type === 'Row') {
    const children = props.children as { explicitList?: string[] } | undefined
    return <div className="a2ui-row">{children?.explicitList?.map(renderById)}</div>
  }

  if (type === 'Card') {
    return <div className="a2ui-card">{typeof props.child === 'string' ? renderById(props.child) : null}</div>
  }

  const Registered = registry.get(type)
  if (Registered) {
    return <Registered node={props} data={surface.data} />
  }

  return (
    <GenericVisualization componentId={type} node={props} />
  )
}

export function A2UISurface({ surface }: { surface: SurfaceState }) {
  const renderById = (id: string): ReactNode => {
    const node = surface.components[id]
    if (!node) return null

    const typed = getComponentType(node)
    if (!typed) return null

    const [type, props] = typed
    return <div key={id}>{renderBuiltIn(type, props, surface, renderById)}</div>
  }

  if (!surface.root) return null

  return <div className="a2ui-surface">{renderById(surface.root)}</div>
}
