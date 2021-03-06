{
  'targets': [
    {
      'target_name': 'profiler',
      'sources': [
        'src/profiler.cc',
        'src/cpu_profiler.cc',
        'src/cpu_profile.cc',
        'src/cpu_profile_node.cc',
        'src/heap_profiler.cc',
        'src/heap_snapshot.cc',
        'src/heap_output_stream.cc',
        'src/heap_graph_node.cc',
        'src/heap_graph_edge.cc'
      ],
      'include_dirs' : [
        "<!(node -e \"require('nan')\")"
      ]
    }
  ]
}
