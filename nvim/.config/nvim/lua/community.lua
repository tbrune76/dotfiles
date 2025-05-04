-- if true then return {} end -- WARN: REMOVE THIS LINE TO ACTIVATE THIS FILE

-- AstroCommunity: import any community modules here
-- We import this file in `lazy_setup.lua` before the `plugins/` folder.
-- This guarantees that the specs are processed before any user plugins.

---@type LazySpec
return {
  "AstroNvim/astrocommunity",
  { import = "astrocommunity.pack.lua" },
  -- { import = "astrocommunity.colorscheme.gruvbox-baby" },
  { import = "astrocommunity.editing-support.undotree" },
  { import = "astrocommunity.editing-support.rainbow-delimiters-nvim" },
  { import = "astrocommunity.color.nvim-highlight-colors" },
  { import = "astrocommunity.git.git-blame-nvim" },
  -- import/override with your plugins folder
}
