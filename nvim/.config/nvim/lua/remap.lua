-- [[ Basic Keymaps ]]
-- Set <space> as the leader key
-- See `:help mapleader`
--  NOTE: Must happen before plugins are required (otherwise wrong leader will be used)
vim.g.mapleader = ' '
vim.g.maplocalleader = ' '

-- Keymaps for better default experience
-- See `:help vim.keymap.set()`
vim.keymap.set({ 'n', 'v' }, '<Space>', '<Nop>', { silent = true })

-- Remap for dealing with word wrap
vim.keymap.set('n', 'k', "v:count == 0 ? 'gk' : 'k'", { expr = true, silent = true })
vim.keymap.set('n', 'j', "v:count == 0 ? 'gj' : 'j'", { expr = true, silent = true })

-- See `:help telescope.builtin`
vim.keymap.set('n', '<leader>?', require('telescope.builtin').oldfiles, { desc = '[?] Find recently opened files' })
vim.keymap.set('n', '<leader><space>', require('telescope.builtin').buffers, { desc = '[ ] Find existing buffers' })
vim.keymap.set('n', '<leader>/', function()
  -- You can pass additional configuration to telescope to change theme, layout, etc.
  require('telescope.builtin').current_buffer_fuzzy_find(require('telescope.themes').get_dropdown {
    winblend = 10,
    previewer = false,
  })
end, { desc = '[/] Fuzzily search in current buffer]' })

vim.keymap.set('n', '<leader>ff', require('telescope.builtin').find_files, { desc = '[F]ind [F]iles' })
vim.keymap.set('n', '<leader>fg', require('telescope.builtin').git_files, { desc = '[F]ind [G]it Fies' })
vim.keymap.set('n', '<leader>fl', require('telescope.builtin').live_grep, { desc = '[F]ind by [L]ive Grep' })
vim.keymap.set('n', '<leader>fh', require('telescope.builtin').help_tags, { desc = '[F]ind [H]elp' })
vim.keymap.set('n', '<leader>fd', require('telescope.builtin').diagnostics, { desc = '[F]ind [D]iagnostics' })

-- Remaps
-- Move Visual Highlight
vim.keymap.set("v", "J", ":m '>+1<CR>gv=gv")
vim.keymap.set("v", "K", ":m '<-2<CR>gv=gv")

-- Halfpage Scrolling stays in middle
vim.keymap.set('n', '<C-d>', '<C-d>zz')
vim.keymap.set('n', '<C-u>', '<C-u>zz')

-- Searchterm stays in middle
vim.keymap.set('n', 'n', 'nzzzv')
vim.keymap.set('n', 'N', 'Nzzzv')

-- Keep Cursor in place when deleting line End
vim.keymap.set('n', 'J', "mzJ'z")

vim.keymap.set('x', '<leader>p', [["_dP]], {desc ='[P]aste over w/o yank'})
vim.keymap.set({"n", "v"}, "<leader>y", [["+y]], {desc='[Y]ank to Clipboard'})
--vim.keymap.set("n", "<leader>Y", [["+Y]]) --?
vim.keymap.set({"n", "v"}, "<leader>d", [["_d]], {desc='[D]elete to Void'})
vim.keymap.set("n", "<leader>r", [[:%s/\<<C-r><C-w>\>/<C-r><C-w>/gI<Left><Left><Left>]], { desc = '[R]eplace' })

vim.keymap.set("n", "<leader>lf", vim.lsp.buf.format, {desc ='LSP: [F]ormat'})


local wk = require("which-key")
wk.register({
  ["<leader>"] = {
    f = {
      name = "+Find",
    },
    g = {
      name = "+Git",
      g = { "<cmd>LazyGit<cr>", "LazyGit" }
    },
    D = {
      name = "+Diagnostics",
      e = { "Open Float" },
      q = { "Set Loclist" },
    },
    l = {
      name = "+LSP",
      c = { "Code" },
      d = { "Document" },
      f = { "Format" },
      r = { "Rename" },
      w = { "Workspace" },
    },
    u = {"<cmd>UndotreeToggle<cr>", "[U]ndotree Toggle", noremap=true},
  },
})
