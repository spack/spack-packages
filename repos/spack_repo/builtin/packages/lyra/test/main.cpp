// -------------------------------------------------------------------------------------------------
// SPDX-License-Identifier: Apache-2.0 OR MIT
// -------------------------------------------------------------------------------------------------
#include <lyra/lyra.hpp>

int main(int argc, const char **argv) {
    bool help = false;
    auto cli = lyra::help(help);
    auto result = cli.parse({argc, argv});
    return result ? 0 : 1;
}
