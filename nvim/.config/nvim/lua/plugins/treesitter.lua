-- if true then return {} end -- WARN: REMOVE THIS LINE TO ACTIVATE THIS FILE

-- Customize Treesitter

---@type LazySpec
return {
  "nvim-treesitter/nvim-treesitter",
  opts = {
    ensure_installed = {
      "lua",
      "vim",
      "bash",
      "c",
      "javascript",
      "json",
      "python",
      "css",
      "csv",
      "rust",
      "java",
      "yaml",
      "hyprlang",
      "arduino",
      "clojure",
      "go",
      "html",
      "jinja",
      "jinja_inline",
      "make",
      "sql",
      "ssh_config",
      "xml",
      -- add more arguments for adding more treesitter parsers
    },
  },
}
