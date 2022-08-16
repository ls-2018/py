#!/usr/bin/env python
# -*- coding: latin-1 -*-

# Fonts:

fpdf_charwidths = {}

fpdf_charwidths['courier'] = {}

for i in range(0, 256):
    fpdf_charwidths['courier'][chr(i)] = 600
    fpdf_charwidths['courierB'] = fpdf_charwidths['courier']
    fpdf_charwidths['courierI'] = fpdf_charwidths['courier']
    fpdf_charwidths['courierBI'] = fpdf_charwidths['courier']

fpdf_charwidths['helvetica'] = {
    '\x00': 278, '\x01': 278, '\x02': 278, '\x03': 278, '\x04': 278, '\x05': 278, '\x06': 278, '\x07': 278, '\x08': 278,
    '\t': 278, '\n': 278, '\x0b': 278, '\x0c': 278, '\r': 278, '\x0e': 278, '\x0f': 278, '\x10': 278, '\x11': 278,
    '\x12': 278, '\x13': 278, '\x14': 278, '\x15': 278,
    '\x16': 278, '\x17': 278, '\x18': 278, '\x19': 278, '\x1a': 278, '\x1b': 278, '\x1c': 278, '\x1d': 278, '\x1e': 278,
    '\x1f': 278, ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667, '\'': 191, '(': 333, ')': 333,
    '*': 389, '+': 584,
    ',': 278, '-': 333, '.': 278, '/': 278, '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556,
    '7': 556, '8': 556, '9': 556, ':': 278, ';': 278, '<': 584, '=': 584, '>': 584, '?': 556, '@': 1015, 'A': 667,
    'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722, 'I': 278, 'J': 500, 'K': 667, 'L': 556,
    'M': 833, 'N': 722, 'O': 778, 'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 278, '\\': 278, ']': 278, '^': 469, '_': 556, '`': 333, 'a': 556, 'b': 556,
    'c': 500, 'd': 556, 'e': 556, 'f': 278, 'g': 556, 'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222, 'm': 833,
    'n': 556, 'o': 556, 'p': 556, 'q': 556, 'r': 333, 's': 500, 't': 278, 'u': 556, 'v': 500, 'w': 722, 'x': 500,
    'y': 500, 'z': 500, '{': 334, '|': 260, '}': 334, '~': 584, '\x7f': 350, '\x80': 556, '\x81': 350, '\x82': 222,
    '\x83': 556,
    '\x84': 333, '\x85': 1000, '\x86': 556, '\x87': 556, '\x88': 333, '\x89': 1000, '\x8a': 667, '\x8b': 333,
    '\x8c': 1000, '\x8d': 350, '\x8e': 611, '\x8f': 350, '\x90': 350, '\x91': 222, '\x92': 222, '\x93': 333,
    '\x94': 333, '\x95': 350, '\x96': 556, '\x97': 1000, '\x98': 333, '\x99': 1000,
    '\x9a': 500, '\x9b': 333, '\x9c': 944, '\x9d': 350, '\x9e': 500, '\x9f': 667, '\xa0': 278, '\xa1': 333, '\xa2': 556,
    '\xa3': 556, '\xa4': 556, '\xa5': 556, '\xa6': 260, '\xa7': 556, '\xa8': 333, '\xa9': 737, '\xaa': 370, '\xab': 556,
    '\xac': 584, '\xad': 333, '\xae': 737, '\xaf': 333,
    '\xb0': 400, '\xb1': 584, '\xb2': 333, '\xb3': 333, '\xb4': 333, '\xb5': 556, '\xb6': 537, '\xb7': 278, '\xb8': 333,
    '\xb9': 333, '\xba': 365, '\xbb': 556, '\xbc': 834, '\xbd': 834, '\xbe': 834, '\xbf': 611, '\xc0': 667, '\xc1': 667,
    '\xc2': 667, '\xc3': 667, '\xc4': 667, '\xc5': 667,
    '\xc6': 1000, '\xc7': 722, '\xc8': 667, '\xc9': 667, '\xca': 667, '\xcb': 667, '\xcc': 278, '\xcd': 278,
    '\xce': 278, '\xcf': 278, '\xd0': 722, '\xd1': 722, '\xd2': 778, '\xd3': 778, '\xd4': 778, '\xd5': 778, '\xd6': 778,
    '\xd7': 584, '\xd8': 778, '\xd9': 722, '\xda': 722, '\xdb': 722,
    '\xdc': 722, '\xdd': 667, '\xde': 667, '\xdf': 611, '\xe0': 556, '\xe1': 556, '\xe2': 556, '\xe3': 556, '\xe4': 556,
    '\xe5': 556, '\xe6': 889, '\xe7': 500, '\xe8': 556, '\xe9': 556, '\xea': 556, '\xeb': 556, '\xec': 278, '\xed': 278,
    '\xee': 278, '\xef': 278, '\xf0': 556, '\xf1': 556,
    '\xf2': 556, '\xf3': 556, '\xf4': 556, '\xf5': 556, '\xf6': 556, '\xf7': 584, '\xf8': 611, '\xf9': 556, '\xfa': 556,
    '\xfb': 556, '\xfc': 556, '\xfd': 500, '\xfe': 556, '\xff': 500}

fpdf_charwidths['helveticaB'] = {
    '\x00': 278, '\x01': 278, '\x02': 278, '\x03': 278, '\x04': 278, '\x05': 278, '\x06': 278, '\x07': 278, '\x08': 278,
    '\t': 278, '\n': 278, '\x0b': 278, '\x0c': 278, '\r': 278, '\x0e': 278, '\x0f': 278, '\x10': 278, '\x11': 278,
    '\x12': 278, '\x13': 278, '\x14': 278, '\x15': 278,
    '\x16': 278, '\x17': 278, '\x18': 278, '\x19': 278, '\x1a': 278, '\x1b': 278, '\x1c': 278, '\x1d': 278, '\x1e': 278,
    '\x1f': 278, ' ': 278, '!': 333, '"': 474, '#': 556, '$': 556, '%': 889, '&': 722, '\'': 238, '(': 333, ')': 333,
    '*': 389, '+': 584,
    ',': 278, '-': 333, '.': 278, '/': 278, '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556,
    '7': 556, '8': 556, '9': 556, ':': 333, ';': 333, '<': 584, '=': 584, '>': 584, '?': 611, '@': 975, 'A': 722,
    'B': 722, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722, 'I': 278, 'J': 556, 'K': 722, 'L': 611,
    'M': 833, 'N': 722, 'O': 778, 'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 333, '\\': 278, ']': 333, '^': 584, '_': 556, '`': 333, 'a': 556, 'b': 611,
    'c': 556, 'd': 611, 'e': 556, 'f': 333, 'g': 611, 'h': 611, 'i': 278, 'j': 278, 'k': 556, 'l': 278, 'm': 889,
    'n': 611, 'o': 611, 'p': 611, 'q': 611, 'r': 389, 's': 556, 't': 333, 'u': 611, 'v': 556, 'w': 778, 'x': 556,
    'y': 556, 'z': 500, '{': 389, '|': 280, '}': 389, '~': 584, '\x7f': 350, '\x80': 556, '\x81': 350, '\x82': 278,
    '\x83': 556,
    '\x84': 500, '\x85': 1000, '\x86': 556, '\x87': 556, '\x88': 333, '\x89': 1000, '\x8a': 667, '\x8b': 333,
    '\x8c': 1000, '\x8d': 350, '\x8e': 611, '\x8f': 350, '\x90': 350, '\x91': 278, '\x92': 278, '\x93': 500,
    '\x94': 500, '\x95': 350, '\x96': 556, '\x97': 1000, '\x98': 333, '\x99': 1000,
    '\x9a': 556, '\x9b': 333, '\x9c': 944, '\x9d': 350, '\x9e': 500, '\x9f': 667, '\xa0': 278, '\xa1': 333, '\xa2': 556,
    '\xa3': 556, '\xa4': 556, '\xa5': 556, '\xa6': 280, '\xa7': 556, '\xa8': 333, '\xa9': 737, '\xaa': 370, '\xab': 556,
    '\xac': 584, '\xad': 333, '\xae': 737, '\xaf': 333,
    '\xb0': 400, '\xb1': 584, '\xb2': 333, '\xb3': 333, '\xb4': 333, '\xb5': 611, '\xb6': 556, '\xb7': 278, '\xb8': 333,
    '\xb9': 333, '\xba': 365, '\xbb': 556, '\xbc': 834, '\xbd': 834, '\xbe': 834, '\xbf': 611, '\xc0': 722, '\xc1': 722,
    '\xc2': 722, '\xc3': 722, '\xc4': 722, '\xc5': 722,
    '\xc6': 1000, '\xc7': 722, '\xc8': 667, '\xc9': 667, '\xca': 667, '\xcb': 667, '\xcc': 278, '\xcd': 278,
    '\xce': 278, '\xcf': 278, '\xd0': 722, '\xd1': 722, '\xd2': 778, '\xd3': 778, '\xd4': 778, '\xd5': 778, '\xd6': 778,
    '\xd7': 584, '\xd8': 778, '\xd9': 722, '\xda': 722, '\xdb': 722,
    '\xdc': 722, '\xdd': 667, '\xde': 667, '\xdf': 611, '\xe0': 556, '\xe1': 556, '\xe2': 556, '\xe3': 556, '\xe4': 556,
    '\xe5': 556, '\xe6': 889, '\xe7': 556, '\xe8': 556, '\xe9': 556, '\xea': 556, '\xeb': 556, '\xec': 278, '\xed': 278,
    '\xee': 278, '\xef': 278, '\xf0': 611, '\xf1': 611,
    '\xf2': 611, '\xf3': 611, '\xf4': 611, '\xf5': 611, '\xf6': 611, '\xf7': 584, '\xf8': 611, '\xf9': 611, '\xfa': 611,
    '\xfb': 611, '\xfc': 611, '\xfd': 556, '\xfe': 611, '\xff': 556
}

fpdf_charwidths['helveticaBI'] = {
    '\x00': 278, '\x01': 278, '\x02': 278, '\x03': 278, '\x04': 278, '\x05': 278, '\x06': 278, '\x07': 278, '\x08': 278,
    '\t': 278, '\n': 278, '\x0b': 278, '\x0c': 278, '\r': 278, '\x0e': 278, '\x0f': 278, '\x10': 278, '\x11': 278,
    '\x12': 278, '\x13': 278, '\x14': 278, '\x15': 278,
    '\x16': 278, '\x17': 278, '\x18': 278, '\x19': 278, '\x1a': 278, '\x1b': 278, '\x1c': 278, '\x1d': 278, '\x1e': 278,
    '\x1f': 278, ' ': 278, '!': 333, '"': 474, '#': 556, '$': 556, '%': 889, '&': 722, '\'': 238, '(': 333, ')': 333,
    '*': 389, '+': 584,
    ',': 278, '-': 333, '.': 278, '/': 278, '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556,
    '7': 556, '8': 556, '9': 556, ':': 333, ';': 333, '<': 584, '=': 584, '>': 584, '?': 611, '@': 975, 'A': 722,
    'B': 722, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722, 'I': 278, 'J': 556, 'K': 722, 'L': 611,
    'M': 833, 'N': 722, 'O': 778, 'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 333, '\\': 278, ']': 333, '^': 584, '_': 556, '`': 333, 'a': 556, 'b': 611,
    'c': 556, 'd': 611, 'e': 556, 'f': 333, 'g': 611, 'h': 611, 'i': 278, 'j': 278, 'k': 556, 'l': 278, 'm': 889,
    'n': 611, 'o': 611, 'p': 611, 'q': 611, 'r': 389, 's': 556, 't': 333, 'u': 611, 'v': 556, 'w': 778, 'x': 556,
    'y': 556, 'z': 500, '{': 389, '|': 280, '}': 389, '~': 584, '\x7f': 350, '\x80': 556, '\x81': 350, '\x82': 278,
    '\x83': 556,
    '\x84': 500, '\x85': 1000, '\x86': 556, '\x87': 556, '\x88': 333, '\x89': 1000, '\x8a': 667, '\x8b': 333,
    '\x8c': 1000, '\x8d': 350, '\x8e': 611, '\x8f': 350, '\x90': 350, '\x91': 278, '\x92': 278, '\x93': 500,
    '\x94': 500, '\x95': 350, '\x96': 556, '\x97': 1000, '\x98': 333, '\x99': 1000,
    '\x9a': 556, '\x9b': 333, '\x9c': 944, '\x9d': 350, '\x9e': 500, '\x9f': 667, '\xa0': 278, '\xa1': 333, '\xa2': 556,
    '\xa3': 556, '\xa4': 556, '\xa5': 556, '\xa6': 280, '\xa7': 556, '\xa8': 333, '\xa9': 737, '\xaa': 370, '\xab': 556,
    '\xac': 584, '\xad': 333, '\xae': 737, '\xaf': 333,
    '\xb0': 400, '\xb1': 584, '\xb2': 333, '\xb3': 333, '\xb4': 333, '\xb5': 611, '\xb6': 556, '\xb7': 278, '\xb8': 333,
    '\xb9': 333, '\xba': 365, '\xbb': 556, '\xbc': 834, '\xbd': 834, '\xbe': 834, '\xbf': 611, '\xc0': 722, '\xc1': 722,
    '\xc2': 722, '\xc3': 722, '\xc4': 722, '\xc5': 722,
    '\xc6': 1000, '\xc7': 722, '\xc8': 667, '\xc9': 667, '\xca': 667, '\xcb': 667, '\xcc': 278, '\xcd': 278,
    '\xce': 278, '\xcf': 278, '\xd0': 722, '\xd1': 722, '\xd2': 778, '\xd3': 778, '\xd4': 778, '\xd5': 778, '\xd6': 778,
    '\xd7': 584, '\xd8': 778, '\xd9': 722, '\xda': 722, '\xdb': 722,
    '\xdc': 722, '\xdd': 667, '\xde': 667, '\xdf': 611, '\xe0': 556, '\xe1': 556, '\xe2': 556, '\xe3': 556, '\xe4': 556,
    '\xe5': 556, '\xe6': 889, '\xe7': 556, '\xe8': 556, '\xe9': 556, '\xea': 556, '\xeb': 556, '\xec': 278, '\xed': 278,
    '\xee': 278, '\xef': 278, '\xf0': 611, '\xf1': 611,
    '\xf2': 611, '\xf3': 611, '\xf4': 611, '\xf5': 611, '\xf6': 611, '\xf7': 584, '\xf8': 611, '\xf9': 611, '\xfa': 611,
    '\xfb': 611, '\xfc': 611, '\xfd': 556, '\xfe': 611, '\xff': 556}

fpdf_charwidths['helveticaI'] = {
    '\x00': 278, '\x01': 278, '\x02': 278, '\x03': 278, '\x04': 278, '\x05': 278, '\x06': 278, '\x07': 278, '\x08': 278,
    '\t': 278, '\n': 278, '\x0b': 278, '\x0c': 278, '\r': 278, '\x0e': 278, '\x0f': 278, '\x10': 278, '\x11': 278,
    '\x12': 278, '\x13': 278, '\x14': 278, '\x15': 278,
    '\x16': 278, '\x17': 278, '\x18': 278, '\x19': 278, '\x1a': 278, '\x1b': 278, '\x1c': 278, '\x1d': 278, '\x1e': 278,
    '\x1f': 278, ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667, '\'': 191, '(': 333, ')': 333,
    '*': 389, '+': 584,
    ',': 278, '-': 333, '.': 278, '/': 278, '0': 556, '1': 556, '2': 556, '3': 556, '4': 556, '5': 556, '6': 556,
    '7': 556, '8': 556, '9': 556, ':': 278, ';': 278, '<': 584, '=': 584, '>': 584, '?': 556, '@': 1015, 'A': 667,
    'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722, 'I': 278, 'J': 500, 'K': 667, 'L': 556,
    'M': 833, 'N': 722, 'O': 778, 'P': 667, 'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 278, '\\': 278, ']': 278, '^': 469, '_': 556, '`': 333, 'a': 556, 'b': 556,
    'c': 500, 'd': 556, 'e': 556, 'f': 278, 'g': 556, 'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222, 'm': 833,
    'n': 556, 'o': 556, 'p': 556, 'q': 556, 'r': 333, 's': 500, 't': 278, 'u': 556, 'v': 500, 'w': 722, 'x': 500,
    'y': 500, 'z': 500, '{': 334, '|': 260, '}': 334, '~': 584, '\x7f': 350, '\x80': 556, '\x81': 350, '\x82': 222,
    '\x83': 556,
    '\x84': 333, '\x85': 1000, '\x86': 556, '\x87': 556, '\x88': 333, '\x89': 1000, '\x8a': 667, '\x8b': 333,
    '\x8c': 1000, '\x8d': 350, '\x8e': 611, '\x8f': 350, '\x90': 350, '\x91': 222, '\x92': 222, '\x93': 333,
    '\x94': 333, '\x95': 350, '\x96': 556, '\x97': 1000, '\x98': 333, '\x99': 1000,
    '\x9a': 500, '\x9b': 333, '\x9c': 944, '\x9d': 350, '\x9e': 500, '\x9f': 667, '\xa0': 278, '\xa1': 333, '\xa2': 556,
    '\xa3': 556, '\xa4': 556, '\xa5': 556, '\xa6': 260, '\xa7': 556, '\xa8': 333, '\xa9': 737, '\xaa': 370, '\xab': 556,
    '\xac': 584, '\xad': 333, '\xae': 737, '\xaf': 333,
    '\xb0': 400, '\xb1': 584, '\xb2': 333, '\xb3': 333, '\xb4': 333, '\xb5': 556, '\xb6': 537, '\xb7': 278, '\xb8': 333,
    '\xb9': 333, '\xba': 365, '\xbb': 556, '\xbc': 834, '\xbd': 834, '\xbe': 834, '\xbf': 611, '\xc0': 667, '\xc1': 667,
    '\xc2': 667, '\xc3': 667, '\xc4': 667, '\xc5': 667,
    '\xc6': 1000, '\xc7': 722, '\xc8': 667, '\xc9': 667, '\xca': 667, '\xcb': 667, '\xcc': 278, '\xcd': 278,
    '\xce': 278, '\xcf': 278, '\xd0': 722, '\xd1': 722, '\xd2': 778, '\xd3': 778, '\xd4': 778, '\xd5': 778, '\xd6': 778,
    '\xd7': 584, '\xd8': 778, '\xd9': 722, '\xda': 722, '\xdb': 722,
    '\xdc': 722, '\xdd': 667, '\xde': 667, '\xdf': 611, '\xe0': 556, '\xe1': 556, '\xe2': 556, '\xe3': 556, '\xe4': 556,
    '\xe5': 556, '\xe6': 889, '\xe7': 500, '\xe8': 556, '\xe9': 556, '\xea': 556, '\xeb': 556, '\xec': 278, '\xed': 278,
    '\xee': 278, '\xef': 278, '\xf0': 556, '\xf1': 556,
    '\xf2': 556, '\xf3': 556, '\xf4': 556, '\xf5': 556, '\xf6': 556, '\xf7': 584, '\xf8': 611, '\xf9': 556, '\xfa': 556,
    '\xfb': 556, '\xfc': 556, '\xfd': 500, '\xfe': 556, '\xff': 500}

fpdf_charwidths['symbol'] = {
    '\x00': 250, '\x01': 250, '\x02': 250, '\x03': 250, '\x04': 250, '\x05': 250, '\x06': 250, '\x07': 250, '\x08': 250,
    '\t': 250, '\n': 250, '\x0b': 250, '\x0c': 250, '\r': 250, '\x0e': 250, '\x0f': 250, '\x10': 250, '\x11': 250,
    '\x12': 250, '\x13': 250, '\x14': 250, '\x15': 250,
    '\x16': 250, '\x17': 250, '\x18': 250, '\x19': 250, '\x1a': 250, '\x1b': 250, '\x1c': 250, '\x1d': 250, '\x1e': 250,
    '\x1f': 250, ' ': 250, '!': 333, '"': 713, '#': 500, '$': 549, '%': 833, '&': 778, '\'': 439, '(': 333, ')': 333,
    '*': 500, '+': 549,
    ',': 250, '-': 549, '.': 250, '/': 278, '0': 500, '1': 500, '2': 500, '3': 500, '4': 500, '5': 500, '6': 500,
    '7': 500, '8': 500, '9': 500, ':': 278, ';': 278, '<': 549, '=': 549, '>': 549, '?': 444, '@': 549, 'A': 722,
    'B': 667, 'C': 722, 'D': 612, 'E': 611, 'F': 763, 'G': 603, 'H': 722, 'I': 333, 'J': 631, 'K': 722, 'L': 686,
    'M': 889, 'N': 722, 'O': 722, 'P': 768, 'Q': 741, 'R': 556, 'S': 592, 'T': 611, 'U': 690, 'V': 439, 'W': 768,
    'X': 645, 'Y': 795, 'Z': 611, '[': 333, '\\': 863, ']': 333, '^': 658, '_': 500, '`': 500, 'a': 631, 'b': 549,
    'c': 549, 'd': 494, 'e': 439, 'f': 521, 'g': 411, 'h': 603, 'i': 329, 'j': 603, 'k': 549, 'l': 549, 'm': 576,
    'n': 521, 'o': 549, 'p': 549, 'q': 521, 'r': 549, 's': 603, 't': 439, 'u': 576, 'v': 713, 'w': 686, 'x': 493,
    'y': 686, 'z': 494, '{': 480, '|': 200, '}': 480, '~': 549, '\x7f': 0, '\x80': 0, '\x81': 0, '\x82': 0, '\x83': 0,
    '\x84': 0, '\x85': 0, '\x86': 0, '\x87': 0, '\x88': 0, '\x89': 0, '\x8a': 0, '\x8b': 0, '\x8c': 0, '\x8d': 0,
    '\x8e': 0, '\x8f': 0, '\x90': 0, '\x91': 0, '\x92': 0, '\x93': 0, '\x94': 0, '\x95': 0, '\x96': 0, '\x97': 0,
    '\x98': 0, '\x99': 0,
    '\x9a': 0, '\x9b': 0, '\x9c': 0, '\x9d': 0, '\x9e': 0, '\x9f': 0, '\xa0': 750, '\xa1': 620, '\xa2': 247,
    '\xa3': 549, '\xa4': 167, '\xa5': 713, '\xa6': 500, '\xa7': 753, '\xa8': 753, '\xa9': 753, '\xaa': 753,
    '\xab': 1042, '\xac': 987, '\xad': 603, '\xae': 987, '\xaf': 603,
    '\xb0': 400, '\xb1': 549, '\xb2': 411, '\xb3': 549, '\xb4': 549, '\xb5': 713, '\xb6': 494, '\xb7': 460, '\xb8': 549,
    '\xb9': 549, '\xba': 549, '\xbb': 549, '\xbc': 1000, '\xbd': 603, '\xbe': 1000, '\xbf': 658, '\xc0': 823,
    '\xc1': 686, '\xc2': 795, '\xc3': 987, '\xc4': 768, '\xc5': 768,
    '\xc6': 823, '\xc7': 768, '\xc8': 768, '\xc9': 713, '\xca': 713, '\xcb': 713, '\xcc': 713, '\xcd': 713, '\xce': 713,
    '\xcf': 713, '\xd0': 768, '\xd1': 713, '\xd2': 790, '\xd3': 790, '\xd4': 890, '\xd5': 823, '\xd6': 549, '\xd7': 250,
    '\xd8': 713, '\xd9': 603, '\xda': 603, '\xdb': 1042,
    '\xdc': 987, '\xdd': 603, '\xde': 987, '\xdf': 603, '\xe0': 494, '\xe1': 329, '\xe2': 790, '\xe3': 790, '\xe4': 786,
    '\xe5': 713, '\xe6': 384, '\xe7': 384, '\xe8': 384, '\xe9': 384, '\xea': 384, '\xeb': 384, '\xec': 494, '\xed': 494,
    '\xee': 494, '\xef': 494, '\xf0': 0, '\xf1': 329,
    '\xf2': 274, '\xf3': 686, '\xf4': 686, '\xf5': 686, '\xf6': 384, '\xf7': 384, '\xf8': 384, '\xf9': 384, '\xfa': 384,
    '\xfb': 384, '\xfc': 494, '\xfd': 494, '\xfe': 494, '\xff': 0}

fpdf_charwidths['times'] = {
    '\x00': 250, '\x01': 250, '\x02': 250, '\x03': 250, '\x04': 250, '\x05': 250, '\x06': 250, '\x07': 250, '\x08': 250,
    '\t': 250, '\n': 250, '\x0b': 250, '\x0c': 250, '\r': 250, '\x0e': 250, '\x0f': 250, '\x10': 250, '\x11': 250,
    '\x12': 250, '\x13': 250, '\x14': 250, '\x15': 250,
    '\x16': 250, '\x17': 250, '\x18': 250, '\x19': 250, '\x1a': 250, '\x1b': 250, '\x1c': 250, '\x1d': 250, '\x1e': 250,
    '\x1f': 250, ' ': 250, '!': 333, '"': 408, '#': 500, '$': 500, '%': 833, '&': 778, '\'': 180, '(': 333, ')': 333,
    '*': 500, '+': 564,
    ',': 250, '-': 333, '.': 250, '/': 278, '0': 500, '1': 500, '2': 500, '3': 500, '4': 500, '5': 500, '6': 500,
    '7': 500, '8': 500, '9': 500, ':': 278, ';': 278, '<': 564, '=': 564, '>': 564, '?': 444, '@': 921, 'A': 722,
    'B': 667, 'C': 667, 'D': 722, 'E': 611, 'F': 556, 'G': 722, 'H': 722, 'I': 333, 'J': 389, 'K': 722, 'L': 611,
    'M': 889, 'N': 722, 'O': 722, 'P': 556, 'Q': 722, 'R': 667, 'S': 556, 'T': 611, 'U': 722, 'V': 722, 'W': 944,
    'X': 722, 'Y': 722, 'Z': 611, '[': 333, '\\': 278, ']': 333, '^': 469, '_': 500, '`': 333, 'a': 444, 'b': 500,
    'c': 444, 'd': 500, 'e': 444, 'f': 333, 'g': 500, 'h': 500, 'i': 278, 'j': 278, 'k': 500, 'l': 278, 'm': 778,
    'n': 500, 'o': 500, 'p': 500, 'q': 500, 'r': 333, 's': 389, 't': 278, 'u': 500, 'v': 500, 'w': 722, 'x': 500,
    'y': 500, 'z': 444, '{': 480, '|': 200, '}': 480, '~': 541, '\x7f': 350, '\x80': 500, '\x81': 350, '\x82': 333,
    '\x83': 500,
    '\x84': 444, '\x85': 1000, '\x86': 500, '\x87': 500, '\x88': 333, '\x89': 1000, '\x8a': 556, '\x8b': 333,
    '\x8c': 889, '\x8d': 350, '\x8e': 611, '\x8f': 350, '\x90': 350, '\x91': 333, '\x92': 333, '\x93': 444, '\x94': 444,
    '\x95': 350, '\x96': 500, '\x97': 1000, '\x98': 333, '\x99': 980,
    '\x9a': 389, '\x9b': 333, '\x9c': 722, '\x9d': 350, '\x9e': 444, '\x9f': 722, '\xa0': 250, '\xa1': 333, '\xa2': 500,
    '\xa3': 500, '\xa4': 500, '\xa5': 500, '\xa6': 200, '\xa7': 500, '\xa8': 333, '\xa9': 760, '\xaa': 276, '\xab': 500,
    '\xac': 564, '\xad': 333, '\xae': 760, '\xaf': 333,
    '\xb0': 400, '\xb1': 564, '\xb2': 300, '\xb3': 300, '\xb4': 333, '\xb5': 500, '\xb6': 453, '\xb7': 250, '\xb8': 333,
    '\xb9': 300, '\xba': 310, '\xbb': 500, '\xbc': 750, '\xbd': 750, '\xbe': 750, '\xbf': 444, '\xc0': 722, '\xc1': 722,
    '\xc2': 722, '\xc3': 722, '\xc4': 722, '\xc5': 722,
    '\xc6': 889, '\xc7': 667, '\xc8': 611, '\xc9': 611, '\xca': 611, '\xcb': 611, '\xcc': 333, '\xcd': 333, '\xce': 333,
    '\xcf': 333, '\xd0': 722, '\xd1': 722, '\xd2': 722, '\xd3': 722, '\xd4': 722, '\xd5': 722, '\xd6': 722, '\xd7': 564,
    '\xd8': 722, '\xd9': 722, '\xda': 722, '\xdb': 722,
    '\xdc': 722, '\xdd': 722, '\xde': 556, '\xdf': 500, '\xe0': 444, '\xe1': 444, '\xe2': 444, '\xe3': 444, '\xe4': 444,
    '\xe5': 444, '\xe6': 667, '\xe7': 444, '\xe8': 444, '\xe9': 444, '\xea': 444, '\xeb': 444, '\xec': 278, '\xed': 278,
    '\xee': 278, '\xef': 278, '\xf0': 500, '\xf1': 500,
    '\xf2': 500, '\xf3': 500, '\xf4': 500, '\xf5': 500, '\xf6': 500, '\xf7': 564, '\xf8': 500, '\xf9': 500, '\xfa': 500,
    '\xfb': 500, '\xfc': 500, '\xfd': 500, '\xfe': 500, '\xff': 500}

fpdf_charwidths['timesB'] = {
    '\x00': 250, '\x01': 250, '\x02': 250, '\x03': 250, '\x04': 250, '\x05': 250, '\x06': 250, '\x07': 250, '\x08': 250,
    '\t': 250, '\n': 250, '\x0b': 250, '\x0c': 250, '\r': 250, '\x0e': 250, '\x0f': 250, '\x10': 250, '\x11': 250,
    '\x12': 250, '\x13': 250, '\x14': 250, '\x15': 250,
    '\x16': 250, '\x17': 250, '\x18': 250, '\x19': 250, '\x1a': 250, '\x1b': 250, '\x1c': 250, '\x1d': 250, '\x1e': 250,
    '\x1f': 250, ' ': 250, '!': 333, '"': 555, '#': 500, '$': 500, '%': 1000, '&': 833, '\'': 278, '(': 333, ')': 333,
    '*': 500, '+': 570,
    ',': 250, '-': 333, '.': 250, '/': 278, '0': 500, '1': 500, '2': 500, '3': 500, '4': 500, '5': 500, '6': 500,
    '7': 500, '8': 500, '9': 500, ':': 333, ';': 333, '<': 570, '=': 570, '>': 570, '?': 500, '@': 930, 'A': 722,
    'B': 667, 'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 778, 'I': 389, 'J': 500, 'K': 778, 'L': 667,
    'M': 944, 'N': 722, 'O': 778, 'P': 611, 'Q': 778, 'R': 722, 'S': 556, 'T': 667, 'U': 722, 'V': 722, 'W': 1000,
    'X': 722, 'Y': 722, 'Z': 667, '[': 333, '\\': 278, ']': 333, '^': 581, '_': 500, '`': 333, 'a': 500, 'b': 556,
    'c': 444, 'd': 556, 'e': 444, 'f': 333, 'g': 500, 'h': 556, 'i': 278, 'j': 333, 'k': 556, 'l': 278, 'm': 833,
    'n': 556, 'o': 500, 'p': 556, 'q': 556, 'r': 444, 's': 389, 't': 333, 'u': 556, 'v': 500, 'w': 722, 'x': 500,
    'y': 500, 'z': 444, '{': 394, '|': 220, '}': 394, '~': 520, '\x7f': 350, '\x80': 500, '\x81': 350, '\x82': 333,
    '\x83': 500,
    '\x84': 500, '\x85': 1000, '\x86': 500, '\x87': 500, '\x88': 333, '\x89': 1000, '\x8a': 556, '\x8b': 333,
    '\x8c': 1000, '\x8d': 350, '\x8e': 667, '\x8f': 350, '\x90': 350, '\x91': 333, '\x92': 333, '\x93': 500,
    '\x94': 500, '\x95': 350, '\x96': 500, '\x97': 1000, '\x98': 333, '\x99': 1000,
    '\x9a': 389, '\x9b': 333, '\x9c': 722, '\x9d': 350, '\x9e': 444, '\x9f': 722, '\xa0': 250, '\xa1': 333, '\xa2': 500,
    '\xa3': 500, '\xa4': 500, '\xa5': 500, '\xa6': 220, '\xa7': 500, '\xa8': 333, '\xa9': 747, '\xaa': 300, '\xab': 500,
    '\xac': 570, '\xad': 333, '\xae': 747, '\xaf': 333,
    '\xb0': 400, '\xb1': 570, '\xb2': 300, '\xb3': 300, '\xb4': 333, '\xb5': 556, '\xb6': 540, '\xb7': 250, '\xb8': 333,
    '\xb9': 300, '\xba': 330, '\xbb': 500, '\xbc': 750, '\xbd': 750, '\xbe': 750, '\xbf': 500, '\xc0': 722, '\xc1': 722,
    '\xc2': 722, '\xc3': 722, '\xc4': 722, '\xc5': 722,
    '\xc6': 1000, '\xc7': 722, '\xc8': 667, '\xc9': 667, '\xca': 667, '\xcb': 667, '\xcc': 389, '\xcd': 389,
    '\xce': 389, '\xcf': 389, '\xd0': 722, '\xd1': 722, '\xd2': 778, '\xd3': 778, '\xd4': 778, '\xd5': 778, '\xd6': 778,
    '\xd7': 570, '\xd8': 778, '\xd9': 722, '\xda': 722, '\xdb': 722,
    '\xdc': 722, '\xdd': 722, '\xde': 611, '\xdf': 556, '\xe0': 500, '\xe1': 500, '\xe2': 500, '\xe3': 500, '\xe4': 500,
    '\xe5': 500, '\xe6': 722, '\xe7': 444, '\xe8': 444, '\xe9': 444, '\xea': 444, '\xeb': 444, '\xec': 278, '\xed': 278,
    '\xee': 278, '\xef': 278, '\xf0': 500, '\xf1': 556,
    '\xf2': 500, '\xf3': 500, '\xf4': 500, '\xf5': 500, '\xf6': 500, '\xf7': 570, '\xf8': 500, '\xf9': 556, '\xfa': 556,
    '\xfb': 556, '\xfc': 556, '\xfd': 500, '\xfe': 556, '\xff': 500}

fpdf_charwidths['timesBI'] = {
    '\x00': 250, '\x01': 250, '\x02': 250, '\x03': 250, '\x04': 250, '\x05': 250, '\x06': 250, '\x07': 250, '\x08': 250,
    '\t': 250, '\n': 250, '\x0b': 250, '\x0c': 250, '\r': 250, '\x0e': 250, '\x0f': 250, '\x10': 250, '\x11': 250,
    '\x12': 250, '\x13': 250, '\x14': 250, '\x15': 250,
    '\x16': 250, '\x17': 250, '\x18': 250, '\x19': 250, '\x1a': 250, '\x1b': 250, '\x1c': 250, '\x1d': 250, '\x1e': 250,
    '\x1f': 250, ' ': 250, '!': 389, '"': 555, '#': 500, '$': 500, '%': 833, '&': 778, '\'': 278, '(': 333, ')': 333,
    '*': 500, '+': 570,
    ',': 250, '-': 333, '.': 250, '/': 278, '0': 500, '1': 500, '2': 500, '3': 500, '4': 500, '5': 500, '6': 500,
    '7': 500, '8': 500, '9': 500, ':': 333, ';': 333, '<': 570, '=': 570, '>': 570, '?': 500, '@': 832, 'A': 667,
    'B': 667, 'C': 667, 'D': 722, 'E': 667, 'F': 667, 'G': 722, 'H': 778, 'I': 389, 'J': 500, 'K': 667, 'L': 611,
    'M': 889, 'N': 722, 'O': 722, 'P': 611, 'Q': 722, 'R': 667, 'S': 556, 'T': 611, 'U': 722, 'V': 667, 'W': 889,
    'X': 667, 'Y': 611, 'Z': 611, '[': 333, '\\': 278, ']': 333, '^': 570, '_': 500, '`': 333, 'a': 500, 'b': 500,
    'c': 444, 'd': 500, 'e': 444, 'f': 333, 'g': 500, 'h': 556, 'i': 278, 'j': 278, 'k': 500, 'l': 278, 'm': 778,
    'n': 556, 'o': 500, 'p': 500, 'q': 500, 'r': 389, 's': 389, 't': 278, 'u': 556, 'v': 444, 'w': 667, 'x': 500,
    'y': 444, 'z': 389, '{': 348, '|': 220, '}': 348, '~': 570, '\x7f': 350, '\x80': 500, '\x81': 350, '\x82': 333,
    '\x83': 500,
    '\x84': 500, '\x85': 1000, '\x86': 500, '\x87': 500, '\x88': 333, '\x89': 1000, '\x8a': 556, '\x8b': 333,
    '\x8c': 944, '\x8d': 350, '\x8e': 611, '\x8f': 350, '\x90': 350, '\x91': 333, '\x92': 333, '\x93': 500, '\x94': 500,
    '\x95': 350, '\x96': 500, '\x97': 1000, '\x98': 333, '\x99': 1000,
    '\x9a': 389, '\x9b': 333, '\x9c': 722, '\x9d': 350, '\x9e': 389, '\x9f': 611, '\xa0': 250, '\xa1': 389, '\xa2': 500,
    '\xa3': 500, '\xa4': 500, '\xa5': 500, '\xa6': 220, '\xa7': 500, '\xa8': 333, '\xa9': 747, '\xaa': 266, '\xab': 500,
    '\xac': 606, '\xad': 333, '\xae': 747, '\xaf': 333,
    '\xb0': 400, '\xb1': 570, '\xb2': 300, '\xb3': 300, '\xb4': 333, '\xb5': 576, '\xb6': 500, '\xb7': 250, '\xb8': 333,
    '\xb9': 300, '\xba': 300, '\xbb': 500, '\xbc': 750, '\xbd': 750, '\xbe': 750, '\xbf': 500, '\xc0': 667, '\xc1': 667,
    '\xc2': 667, '\xc3': 667, '\xc4': 667, '\xc5': 667,
    '\xc6': 944, '\xc7': 667, '\xc8': 667, '\xc9': 667, '\xca': 667, '\xcb': 667, '\xcc': 389, '\xcd': 389, '\xce': 389,
    '\xcf': 389, '\xd0': 722, '\xd1': 722, '\xd2': 722, '\xd3': 722, '\xd4': 722, '\xd5': 722, '\xd6': 722, '\xd7': 570,
    '\xd8': 722, '\xd9': 722, '\xda': 722, '\xdb': 722,
    '\xdc': 722, '\xdd': 611, '\xde': 611, '\xdf': 500, '\xe0': 500, '\xe1': 500, '\xe2': 500, '\xe3': 500, '\xe4': 500,
    '\xe5': 500, '\xe6': 722, '\xe7': 444, '\xe8': 444, '\xe9': 444, '\xea': 444, '\xeb': 444, '\xec': 278, '\xed': 278,
    '\xee': 278, '\xef': 278, '\xf0': 500, '\xf1': 556,
    '\xf2': 500, '\xf3': 500, '\xf4': 500, '\xf5': 500, '\xf6': 500, '\xf7': 570, '\xf8': 500, '\xf9': 556, '\xfa': 556,
    '\xfb': 556, '\xfc': 556, '\xfd': 444, '\xfe': 500, '\xff': 444}

fpdf_charwidths['timesI'] = {
    '\x00': 250, '\x01': 250, '\x02': 250, '\x03': 250, '\x04': 250, '\x05': 250, '\x06': 250, '\x07': 250, '\x08': 250,
    '\t': 250, '\n': 250, '\x0b': 250, '\x0c': 250, '\r': 250, '\x0e': 250, '\x0f': 250, '\x10': 250, '\x11': 250,
    '\x12': 250, '\x13': 250, '\x14': 250, '\x15': 250,
    '\x16': 250, '\x17': 250, '\x18': 250, '\x19': 250, '\x1a': 250, '\x1b': 250, '\x1c': 250, '\x1d': 250, '\x1e': 250,
    '\x1f': 250, ' ': 250, '!': 333, '"': 420, '#': 500, '$': 500, '%': 833, '&': 778, '\'': 214, '(': 333, ')': 333,
    '*': 500, '+': 675,
    ',': 250, '-': 333, '.': 250, '/': 278, '0': 500, '1': 500, '2': 500, '3': 500, '4': 500, '5': 500, '6': 500,
    '7': 500, '8': 500, '9': 500, ':': 333, ';': 333, '<': 675, '=': 675, '>': 675, '?': 500, '@': 920, 'A': 611,
    'B': 611, 'C': 667, 'D': 722, 'E': 611, 'F': 611, 'G': 722, 'H': 722, 'I': 333, 'J': 444, 'K': 667, 'L': 556,
    'M': 833, 'N': 667, 'O': 722, 'P': 611, 'Q': 722, 'R': 611, 'S': 500, 'T': 556, 'U': 722, 'V': 611, 'W': 833,
    'X': 611, 'Y': 556, 'Z': 556, '[': 389, '\\': 278, ']': 389, '^': 422, '_': 500, '`': 333, 'a': 500, 'b': 500,
    'c': 444, 'd': 500, 'e': 444, 'f': 278, 'g': 500, 'h': 500, 'i': 278, 'j': 278, 'k': 444, 'l': 278, 'm': 722,
    'n': 500, 'o': 500, 'p': 500, 'q': 500, 'r': 389, 's': 389, 't': 278, 'u': 500, 'v': 444, 'w': 667, 'x': 444,
    'y': 444, 'z': 389, '{': 400, '|': 275, '}': 400, '~': 541, '\x7f': 350, '\x80': 500, '\x81': 350, '\x82': 333,
    '\x83': 500,
    '\x84': 556, '\x85': 889, '\x86': 500, '\x87': 500, '\x88': 333, '\x89': 1000, '\x8a': 500, '\x8b': 333,
    '\x8c': 944, '\x8d': 350, '\x8e': 556, '\x8f': 350, '\x90': 350, '\x91': 333, '\x92': 333, '\x93': 556, '\x94': 556,
    '\x95': 350, '\x96': 500, '\x97': 889, '\x98': 333, '\x99': 980,
    '\x9a': 389, '\x9b': 333, '\x9c': 667, '\x9d': 350, '\x9e': 389, '\x9f': 556, '\xa0': 250, '\xa1': 389, '\xa2': 500,
    '\xa3': 500, '\xa4': 500, '\xa5': 500, '\xa6': 275, '\xa7': 500, '\xa8': 333, '\xa9': 760, '\xaa': 276, '\xab': 500,
    '\xac': 675, '\xad': 333, '\xae': 760, '\xaf': 333,
    '\xb0': 400, '\xb1': 675, '\xb2': 300, '\xb3': 300, '\xb4': 333, '\xb5': 500, '\xb6': 523, '\xb7': 250, '\xb8': 333,
    '\xb9': 300, '\xba': 310, '\xbb': 500, '\xbc': 750, '\xbd': 750, '\xbe': 750, '\xbf': 500, '\xc0': 611, '\xc1': 611,
    '\xc2': 611, '\xc3': 611, '\xc4': 611, '\xc5': 611,
    '\xc6': 889, '\xc7': 667, '\xc8': 611, '\xc9': 611, '\xca': 611, '\xcb': 611, '\xcc': 333, '\xcd': 333, '\xce': 333,
    '\xcf': 333, '\xd0': 722, '\xd1': 667, '\xd2': 722, '\xd3': 722, '\xd4': 722, '\xd5': 722, '\xd6': 722, '\xd7': 675,
    '\xd8': 722, '\xd9': 722, '\xda': 722, '\xdb': 722,
    '\xdc': 722, '\xdd': 556, '\xde': 611, '\xdf': 500, '\xe0': 500, '\xe1': 500, '\xe2': 500, '\xe3': 500, '\xe4': 500,
    '\xe5': 500, '\xe6': 667, '\xe7': 444, '\xe8': 444, '\xe9': 444, '\xea': 444, '\xeb': 444, '\xec': 278, '\xed': 278,
    '\xee': 278, '\xef': 278, '\xf0': 500, '\xf1': 500,
    '\xf2': 500, '\xf3': 500, '\xf4': 500, '\xf5': 500, '\xf6': 500, '\xf7': 675, '\xf8': 500, '\xf9': 500, '\xfa': 500,
    '\xfb': 500, '\xfc': 500, '\xfd': 444, '\xfe': 500, '\xff': 444}

fpdf_charwidths['zapfdingbats'] = {
    '\x00': 0, '\x01': 0, '\x02': 0, '\x03': 0, '\x04': 0, '\x05': 0, '\x06': 0, '\x07': 0, '\x08': 0, '\t': 0, '\n': 0,
    '\x0b': 0, '\x0c': 0, '\r': 0, '\x0e': 0, '\x0f': 0, '\x10': 0, '\x11': 0, '\x12': 0, '\x13': 0, '\x14': 0,
    '\x15': 0,
    '\x16': 0, '\x17': 0, '\x18': 0, '\x19': 0, '\x1a': 0, '\x1b': 0, '\x1c': 0, '\x1d': 0, '\x1e': 0, '\x1f': 0,
    ' ': 278, '!': 974, '"': 961, '#': 974, '$': 980, '%': 719, '&': 789, '\'': 790, '(': 791, ')': 690, '*': 960,
    '+': 939,
    ',': 549, '-': 855, '.': 911, '/': 933, '0': 911, '1': 945, '2': 974, '3': 755, '4': 846, '5': 762, '6': 761,
    '7': 571, '8': 677, '9': 763, ':': 760, ';': 759, '<': 754, '=': 494, '>': 552, '?': 537, '@': 577, 'A': 692,
    'B': 786, 'C': 788, 'D': 788, 'E': 790, 'F': 793, 'G': 794, 'H': 816, 'I': 823, 'J': 789, 'K': 841, 'L': 823,
    'M': 833, 'N': 816, 'O': 831, 'P': 923, 'Q': 744, 'R': 723, 'S': 749, 'T': 790, 'U': 792, 'V': 695, 'W': 776,
    'X': 768, 'Y': 792, 'Z': 759, '[': 707, '\\': 708, ']': 682, '^': 701, '_': 826, '`': 815, 'a': 789, 'b': 789,
    'c': 707, 'd': 687, 'e': 696, 'f': 689, 'g': 786, 'h': 787, 'i': 713, 'j': 791, 'k': 785, 'l': 791, 'm': 873,
    'n': 761, 'o': 762, 'p': 762, 'q': 759, 'r': 759, 's': 892, 't': 892, 'u': 788, 'v': 784, 'w': 438, 'x': 138,
    'y': 277, 'z': 415, '{': 392, '|': 392, '}': 668, '~': 668, '\x7f': 0, '\x80': 390, '\x81': 390, '\x82': 317,
    '\x83': 317,
    '\x84': 276, '\x85': 276, '\x86': 509, '\x87': 509, '\x88': 410, '\x89': 410, '\x8a': 234, '\x8b': 234, '\x8c': 334,
    '\x8d': 334, '\x8e': 0, '\x8f': 0, '\x90': 0, '\x91': 0, '\x92': 0, '\x93': 0, '\x94': 0, '\x95': 0, '\x96': 0,
    '\x97': 0, '\x98': 0, '\x99': 0,
    '\x9a': 0, '\x9b': 0, '\x9c': 0, '\x9d': 0, '\x9e': 0, '\x9f': 0, '\xa0': 0, '\xa1': 732, '\xa2': 544, '\xa3': 544,
    '\xa4': 910, '\xa5': 667, '\xa6': 760, '\xa7': 760, '\xa8': 776, '\xa9': 595, '\xaa': 694, '\xab': 626, '\xac': 788,
    '\xad': 788, '\xae': 788, '\xaf': 788,
    '\xb0': 788, '\xb1': 788, '\xb2': 788, '\xb3': 788, '\xb4': 788, '\xb5': 788, '\xb6': 788, '\xb7': 788, '\xb8': 788,
    '\xb9': 788, '\xba': 788, '\xbb': 788, '\xbc': 788, '\xbd': 788, '\xbe': 788, '\xbf': 788, '\xc0': 788, '\xc1': 788,
    '\xc2': 788, '\xc3': 788, '\xc4': 788, '\xc5': 788,
    '\xc6': 788, '\xc7': 788, '\xc8': 788, '\xc9': 788, '\xca': 788, '\xcb': 788, '\xcc': 788, '\xcd': 788, '\xce': 788,
    '\xcf': 788, '\xd0': 788, '\xd1': 788, '\xd2': 788, '\xd3': 788, '\xd4': 894, '\xd5': 838, '\xd6': 1016,
    '\xd7': 458, '\xd8': 748, '\xd9': 924, '\xda': 748, '\xdb': 918,
    '\xdc': 927, '\xdd': 928, '\xde': 928, '\xdf': 834, '\xe0': 873, '\xe1': 828, '\xe2': 924, '\xe3': 924, '\xe4': 917,
    '\xe5': 930, '\xe6': 931, '\xe7': 463, '\xe8': 883, '\xe9': 836, '\xea': 836, '\xeb': 867, '\xec': 867, '\xed': 696,
    '\xee': 696, '\xef': 874, '\xf0': 0, '\xf1': 874,
    '\xf2': 760, '\xf3': 946, '\xf4': 771, '\xf5': 865, '\xf6': 771, '\xf7': 888, '\xf8': 967, '\xf9': 888, '\xfa': 831,
    '\xfb': 873, '\xfc': 927, '\xfd': 970, '\xfe': 918, '\xff': 0}
