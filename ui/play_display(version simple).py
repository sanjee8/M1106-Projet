# Module play display
# from termcolor import cprint ( à importer )
def get_color(score):
    if(score == 0 or score == 1):
        return 'on_blue'
    elif(score == 2):
        return 'on_red'
    else:
        return 'on_white'

def sized(score):
  if(score > 100):
      return ' '+str(score)+' '
  elif(score > 10):
      return '  '+str(score)+' '
  else:
    return '  '+str(score)+'  '

# module: /ui/play_display ( from termcolor import cprint )
def full_display(plateau):
    #line 1
    cprint('     ', 'grey', get_color(plateau['tiles'][0]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][1]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][2]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][3]))

    cprint(sized(plateau['tiles'][0]), 'grey', get_color(plateau['tiles'][0]), end=' ')
    cprint(sized(plateau['tiles'][1]), 'grey', get_color(plateau['tiles'][1]), end=' ')
    cprint(sized(plateau['tiles'][2]), 'grey', get_color(plateau['tiles'][2]), end=' ')
    cprint(sized(plateau['tiles'][3]), 'grey', get_color(plateau['tiles'][3]))

    cprint('     ', 'grey', get_color(plateau['tiles'][0]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][1]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][2]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][3]))

    cprint('  ')

    #line 2
    cprint('     ', 'grey', get_color(plateau['tiles'][4]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][5]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][6]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][7]))

    cprint(sized(plateau['tiles'][4]), 'grey', get_color(plateau['tiles'][4]), end=' ')
    cprint(sized(plateau['tiles'][5]), 'grey', get_color(plateau['tiles'][5]), end=' ')
    cprint(sized(plateau['tiles'][6]), 'grey', get_color(plateau['tiles'][6]), end=' ')
    cprint(sized(plateau['tiles'][7]), 'grey', get_color(plateau['tiles'][7]))

    cprint('     ', 'grey', get_color(plateau['tiles'][4]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][5]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][6]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][7]))

    cprint('  ')

    #line 3
    cprint('     ', 'grey', get_color(plateau['tiles'][8]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][9]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][10]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][11]))

    cprint(sized(plateau['tiles'][8]), 'grey', get_color(plateau['tiles'][8]), end=' ')
    cprint(sized(plateau['tiles'][9]), 'grey', get_color(plateau['tiles'][9]), end=' ')
    cprint(sized(plateau['tiles'][10]), 'grey', get_color(plateau['tiles'][10]), end=' ')
    cprint(sized(plateau['tiles'][11]), 'grey', get_color(plateau['tiles'][11]))

    cprint('     ', 'grey', get_color(plateau['tiles'][8]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][9]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][10]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][11]))

    cprint('  ')

    #line 4
    cprint('     ', 'grey', get_color(plateau['tiles'][12]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][13]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][14]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][15]))

    cprint(sized(plateau['tiles'][12]), 'grey', get_color(plateau['tiles'][12]), end=' ')
    cprint(sized(plateau['tiles'][13]), 'grey', get_color(plateau['tiles'][13]), end=' ')
    cprint(sized(plateau['tiles'][14]), 'grey', get_color(plateau['tiles'][14]), end=' ')
    cprint(sized(plateau['tiles'][15]), 'grey', get_color(plateau['tiles'][15]))

    cprint('     ', 'grey', get_color(plateau['tiles'][12]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][13]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][14]), end=' ')
    cprint('     ', 'grey', get_color(plateau['tiles'][15]))

