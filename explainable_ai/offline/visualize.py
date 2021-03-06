from IPython.display import display, HTML

def visualize_token_attrs(tokens, attrs):
  """
  Visualize attributions for given set of tokens.
  Args:
  - tokens: An array of tokens
  - attrs: An array of attributions, of same size as 'tokens',
    with attrs[i] being the attribution to tokens[i]
  
  Returns:
  - visualization: An IPython.core.display.HTML object showing
    tokens color-coded based on strength of their attribution.
  """
  def get_color(attr):
    if attr > 0:
      r = int(128*attr) + 127
      g = 128 - int(64*attr)
      b = 128 - int(64*attr) 
    else:
      r = 128 + int(64*attr)
      g = 128 + int(64*attr) 
      b = int(-128*attr) + 127
    return r,g,b

  # normalize attributions for visualization.
  bound = max(abs(attrs.max()), abs(attrs.min()))

  if bound != 0:
    attrs = attrs/bound
  
  html_text = ""
  for i, tok in enumerate(tokens):
    r,g,b = get_color(attrs[i])
    html_text += " <span style='color:rgb(%d,%d,%d)'>%s</span>" % (r, g, b, tok)
  return HTML(html_text)