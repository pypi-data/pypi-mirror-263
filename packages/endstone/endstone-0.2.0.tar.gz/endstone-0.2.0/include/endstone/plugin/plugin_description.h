// Copyright (c) 2023, The Endstone Project. (https://endstone.dev) All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#pragma once

#include <regex>
#include <string>
#include <vector>

#include <fmt/format.h>

namespace endstone {

class PluginDescription {
public:
    PluginDescription(std::string name, std::string version, std::string description = "",
                      std::vector<std::string> authors = {}, std::string prefix = "")
    {
        name_ = std::move(name);
        std::replace(name_.begin(), name_.end(), ' ', '_');
        version_ = std::move(version);
        full_name_ = fmt::format("{} v{}", name_, version_);
        description_ = std::move(description);
        authors_ = std::move(authors);
        prefix_ = std::move(prefix);
    }

    /**
     * Gives the name of the plugin. This name is a unique identifier for plugins.
     *
     * @return the name of the plugin
     */
    [[nodiscard]] const std::string &getName() const
    {
        return name_;
    }

    /**
     * Gives the version of the plugin.
     *
     * @return the version of the plugin
     */
    [[nodiscard]] const std::string &getVersion() const
    {
        return version_;
    }

    /**
     * Returns the name of a plugin, including the version.
     *
     * @return a descriptive name of the plugin and respective version
     */
    [[nodiscard]] const std::string &getFullName() const
    {
        return full_name_;
    }

    /**
     * Gives a human-friendly description of the functionality the plugin provides.
     * @return description of this plugin, or null if not specified
     */
    [[nodiscard]] std::string getDescription() const
    {
        return description_;
    }

    /**
     * Gives the list of authors for the plugin.
     *
     * @return a list of the plugin's authors
     */
    [[nodiscard]] std::vector<std::string> getAuthors() const
    {
        return authors_;
    }

    /**
     * Gives the token to prefix plugin-specific logging messages with.
     *
     * @return the prefixed logging token, or null if not specified
     */
    [[nodiscard]] std::string getPrefix() const
    {
        return prefix_;
    }

    inline const static std::regex VALID_NAME{"^[A-Za-z0-9 _.-]+$"};

private:
    std::string name_;
    std::string version_;
    std::string full_name_;
    std::string description_;
    std::vector<std::string> authors_;
    std::string prefix_;
};

}  // namespace endstone
